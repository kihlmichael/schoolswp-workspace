import * as vscode from 'vscode';
import { getNonce } from './nonce';

export function getWebviewContent(
  webview: vscode.Webview,
  extensionUri: vscode.Uri,
  mode: 'sidebar' | 'panel'
): string {
  const nonce = getNonce();
  const cspSource = webview.cspSource;

  const styleUri = webview.asWebviewUri(
    vscode.Uri.joinPath(extensionUri, 'media', 'webview', 'agent.css')
  );
  const scriptUri = webview.asWebviewUri(
    vscode.Uri.joinPath(extensionUri, 'media', 'webview', 'agent.js')
  );

  return `<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Security-Policy"
    content="default-src 'none';
             img-src ${cspSource} data:;
             script-src 'nonce-${nonce}';
             style-src ${cspSource} 'nonce-${nonce}';
             font-src ${cspSource};
             connect-src 'none';">
  <link href="${styleUri}" rel="stylesheet" nonce="${nonce}">
  <title>Agent Visual</title>
</head>
<body data-mode="${mode}">
  <div id="agent-container" role="application" aria-label="Agent Visual">
    <div id="avatar-stage" role="img" aria-label="Avatar anime">
      <canvas id="avatar-canvas" width="200" height="200"></canvas>
    </div>
    <div id="status-bar" role="status" aria-live="polite">
      <span id="status-text">Pret</span>
      <span id="status-indicator" class="indicator idle"></span>
    </div>
    <div id="chat-area" role="log" aria-label="Conversation">
      <div id="chat-messages"></div>
      <form id="chat-form">
        <input id="chat-input" type="text" placeholder="Parle a l'agent..."
               aria-label="Message" autocomplete="off">
        <button type="submit" aria-label="Envoyer">Envoyer</button>
      </form>
    </div>
    <div id="controls" role="toolbar" aria-label="Controles">
      <button id="btn-pause" aria-label="Pause">Pause</button>
      <button id="btn-speed" aria-label="Vitesse">1x</button>
    </div>
  </div>
  <script nonce="${nonce}" src="${scriptUri}"></script>
</body>
</html>`;
}
