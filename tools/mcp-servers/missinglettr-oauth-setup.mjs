#!/usr/bin/env node
/**
 * Setup one-shot OAuth 2.1 pour Missinglettr MCP.
 *
 * Le serveur Missinglettr expose un MCP HTTP qui exige un Bearer OAuth, mais
 * il ne respecte pas la convention MCP : il renvoie HTTP 200 + JSON-RPC error
 * -32001 au lieu d'un HTTP 401, donc mcp-remote ne declenche jamais son OAuth
 * automatique. On fait la danse OAuth manuellement ici (DCR + PKCE + browser),
 * on cache les tokens, et le launcher du MCP les injectera en Bearer.
 *
 * Usage : node tools/mcp-servers/missinglettr-oauth-setup.mjs
 *         (le navigateur s'ouvre sur /authorize, tu valides, tokens en cache)
 */
import http from 'node:http';
import crypto from 'node:crypto';
import { exec } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '../..');
const ISSUER = 'https://mcp.missinglettr-api.com';
const SCOPE = 'mcp:read mcp:write';
const CRED_FILE = path.join(ROOT, '.credentials/missinglettr-oauth.json');

function b64url(buf) {
  return buf.toString('base64').replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

function findFreePort() {
  return new Promise((resolve, reject) => {
    const srv = http.createServer();
    srv.unref();
    srv.listen(0, '127.0.0.1', () => {
      const port = srv.address().port;
      srv.close(() => resolve(port));
    });
    srv.on('error', reject);
  });
}

async function main() {
  const port = await findFreePort();
  const redirectUri = `http://localhost:${port}/callback`;

  // 1. Dynamic Client Registration
  console.log('[1/4] Registering client...');
  const regResp = await fetch(`${ISSUER}/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      client_name: 'schoolsWP Claude Code',
      redirect_uris: [redirectUri],
      grant_types: ['authorization_code', 'refresh_token'],
      response_types: ['code'],
      token_endpoint_auth_method: 'none',
      scope: SCOPE,
    }),
  });
  if (!regResp.ok) {
    const body = await regResp.text();
    throw new Error(`Register failed: ${regResp.status} — ${body.slice(0, 300)}`);
  }
  const reg = await regResp.json();
  const clientId = reg.client_id;
  console.log(`      client_id obtained (${clientId.slice(0, 8)}...)`);

  // 2. PKCE
  const verifier = b64url(crypto.randomBytes(32));
  const challenge = b64url(crypto.createHash('sha256').update(verifier).digest());
  const state = b64url(crypto.randomBytes(16));

  // 3. Callback server
  const codePromise = new Promise((resolve, reject) => {
    const srv = http.createServer((req, res) => {
      const url = new URL(req.url, `http://localhost:${port}`);
      if (url.pathname !== '/callback') {
        res.writeHead(404).end();
        return;
      }
      const returnedState = url.searchParams.get('state');
      if (returnedState !== state) {
        res.writeHead(400, { 'Content-Type': 'text/html; charset=utf-8' });
        res.end('<h1>State mismatch</h1><p>OAuth flow aborted for security.</p>');
        srv.close();
        return reject(new Error('OAuth state mismatch'));
      }
      const err = url.searchParams.get('error');
      if (err) {
        const desc = url.searchParams.get('error_description') || '';
        res.writeHead(400, { 'Content-Type': 'text/html; charset=utf-8' });
        res.end(`<h1>OAuth error: ${err}</h1><p>${desc}</p>`);
        srv.close();
        return reject(new Error(`${err}: ${desc}`));
      }
      const code = url.searchParams.get('code');
      if (!code) {
        res.writeHead(400).end('<h1>No code</h1>');
        srv.close();
        return reject(new Error('No authorization code in callback'));
      }
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
      res.end(`<!doctype html><html><head><meta charset="utf-8"><title>schoolsWP — Missinglettr OAuth</title>
<style>body{font-family:system-ui;background:#0F1419;color:#F4F5F7;display:flex;align-items:center;justify-content:center;height:100vh;margin:0}
.card{background:#1a1f2a;padding:40px;border-radius:8px;border-left:3px solid #00D400;max-width:480px}
h1{margin:0 0 12px;font-size:20px}p{margin:8px 0;color:#a8b3c1}</style></head>
<body><div class="card"><h1>Authorization OK</h1>
<p>Tokens are being exchanged in your terminal. You can close this tab.</p>
<p style="color:#00D400;margin-top:20px">schoolsWP - Missinglettr connected</p></div></body></html>`);
      srv.close();
      resolve(code);
    });
    srv.listen(port, '127.0.0.1');
    setTimeout(() => {
      srv.close();
      reject(new Error('OAuth flow timed out after 5 minutes'));
    }, 5 * 60 * 1000).unref();
  });

  // 4. Open browser
  const authorizeUrl =
    `${ISSUER}/authorize?` +
    new URLSearchParams({
      response_type: 'code',
      client_id: clientId,
      redirect_uri: redirectUri,
      scope: SCOPE,
      state,
      code_challenge: challenge,
      code_challenge_method: 'S256',
    }).toString();

  console.log(`[2/4] Opening browser on /authorize...`);
  console.log(`      If browser does not open, paste this URL manually:`);
  console.log(`      ${authorizeUrl}`);
  if (process.platform === 'win32') {
    exec(`start "" "${authorizeUrl}"`);
  } else if (process.platform === 'darwin') {
    exec(`open "${authorizeUrl}"`);
  } else {
    exec(`xdg-open "${authorizeUrl}"`);
  }

  // 5. Wait for callback
  console.log('[3/4] Waiting for authorization callback (max 5 min)...');
  const code = await codePromise;
  console.log('      authorization code received');

  // 6. Exchange code -> tokens
  console.log('[4/4] Exchanging code for tokens...');
  const tokenResp = await fetch(`${ISSUER}/token`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      grant_type: 'authorization_code',
      code,
      redirect_uri: redirectUri,
      client_id: clientId,
      code_verifier: verifier,
    }).toString(),
  });
  if (!tokenResp.ok) {
    const body = await tokenResp.text();
    throw new Error(`Token exchange failed: ${tokenResp.status} — ${body.slice(0, 300)}`);
  }
  const tokens = await tokenResp.json();

  fs.mkdirSync(path.dirname(CRED_FILE), { recursive: true });
  fs.writeFileSync(
    CRED_FILE,
    JSON.stringify(
      {
        issuer: ISSUER,
        client_id: clientId,
        redirect_uri: redirectUri,
        access_token: tokens.access_token,
        refresh_token: tokens.refresh_token,
        token_type: tokens.token_type || 'Bearer',
        scope: tokens.scope || SCOPE,
        expires_at: Date.now() + ((tokens.expires_in || 3600) - 60) * 1000,
        saved_at: new Date().toISOString(),
      },
      null,
      2,
    ),
    { mode: 0o600 },
  );

  console.log(`\nTokens cached at: ${path.relative(ROOT, CRED_FILE)}`);
  console.log('Next step: reload Claude Code MCPs (the launcher will inject the Bearer token).');
}

main().catch((err) => {
  console.error('\nOAuth setup failed:', err.message);
  process.exit(1);
});
