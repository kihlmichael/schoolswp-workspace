import { spawn } from 'child_process';
import fs from 'fs';
import path from 'path';

// Charger les secrets de l'environnement depuis settings.local.json
const settingsPath = 'd:/VS Code/CLAUDE CODE/projects/schoolswp/.claude/settings.local.json';
const settings = JSON.parse(fs.readFileSync(settingsPath, 'utf8')).env || {};

const childEnv = { ...process.env };
childEnv['WP_API_URL'] = settings['JOACHIM_WP_API_URL'];
childEnv['WP_API_USERNAME'] = settings['JOACHIM_WP_API_USERNAME'];
childEnv['WP_API_PASSWORD'] = settings['JOACHIM_WP_API_PASSWORD'];

const pkg = '@automattic/mcp-wordpress-remote@0.2.21';

// Le code PHP pour lire le fichier Checkable.php de Fluent Forms
const phpCode = `
global \$wpdb;
\$table = \$wpdb->prefix . 'fluentform_forms';
\$raw = \$wpdb->get_var(\$wpdb->prepare(
    "SELECT form_fields FROM \$table WHERE id = %d",
    5
));

\$form = json_decode(\$raw, true);
if (json_last_error() !== JSON_ERROR_NONE) {
    echo "ERROR: json decode failed: " . json_last_error_msg() . "\\n";
    exit;
}

\$modified = false;
if (isset(\$form['fields']) && is_array(\$form['fields'])) {
    foreach (\$form['fields'] as &\$field) {
        if (\$field['element'] === 'input_radio') {
            if (!isset(\$field['attributes'])) {
                \$field['attributes'] = [];
            }
            if (!isset(\$field['attributes']['type']) || \$field['attributes']['type'] !== 'radio') {
                \$field['attributes']['type'] = 'radio';
                \$modified = true;
                echo "Modified radio field: " . \$field['attributes']['name'] . " - set type=radio\\n";
            }
        }
    }
}

if (\$modified) {
    \$updated_json = wp_json_encode(\$form);
    \$result = \$wpdb->update(\$table, ['form_fields' => \$updated_json], ['id' => 5]);
    if (\$result === false) {
        echo "ERROR: db update failed\\n";
    } else {
        echo "SUCCESS: updated form fields database rows affected: \$result\\n";
        
        // Cache flushing
        if (function_exists('clean_post_cache')) {
            clean_post_cache(91);
            echo "Cleaned post cache for post 91\\n";
        }
        if (function_exists('wp_cache_flush')) {
            wp_cache_flush();
            echo "Flushed WP object cache\\n";
        }
        // LiteSpeed Cache purge
        if (class_exists('LiteSpeed\\\\Purge')) {
            call_user_func(['LiteSpeed\\\\Purge', 'purge_all']);
            echo "Purged LiteSpeed Cache\\n";
        }
        // WP Rocket purge
        if (function_exists('rocket_clean_domain')) {
            rocket_clean_domain();
            echo "Cleaned WP Rocket domain cache\\n";
        }
    }
} else {
    echo "No modifications needed. Radio field already has type=radio.\\n";
}
`;

// Lancer le serveur MCP
console.log("Starting MCP Server for joachimkihl.fr (Read Checkable)...");
const isWin = process.platform === 'win32';
const child = spawn(
  isWin ? 'cmd.exe' : 'npx',
  isWin ? ['/c', 'npx', '-y', pkg] : ['-y', pkg],
  { env: childEnv }
);

let responseBuffer = '';
child.stdout.on('data', (data) => {
  const text = data.toString();
  responseBuffer += text;
  handleResponses();
});

child.stderr.on('data', (data) => {
  console.error("MCP SERVER LOG:", data.toString().trim());
});

child.on('exit', (code) => {
  console.log(`MCP Server exited with code ${code}`);
});

let step = 0;
const messages = [
  // 1. initialize
  {
    jsonrpc: "2.0",
    id: 1,
    method: "initialize",
    params: {
      protocolVersion: "2024-11-05",
      capabilities: {},
      clientInfo: { name: "test-client", version: "1.0" }
    }
  },
  // 2. initialized notification
  {
    jsonrpc: "2.0",
    method: "notifications/initialized"
  },
  // 3. call tool execute-ability
  {
    jsonrpc: "2.0",
    id: 2,
    method: "tools/call",
    params: {
      name: "mcp-adapter-execute-ability",
      arguments: {
        ability_name: "novamira/execute-php",
        parameters: {
          code: phpCode
        }
      }
    }
  }
];

function sendNext() {
  if (step >= messages.length) {
    console.log("All commands sent. Exiting MCP Server...");
    child.stdin.end();
    return;
  }
  
  const msg = messages[step];
  console.log(`Sending step ${step}: ${msg.method || (msg.params && msg.params.name) || 'notification'}`);
  child.stdin.write(JSON.stringify(msg) + "\n");
  step++;
}

// Envoyer la première commande after 2s
setTimeout(sendNext, 2000);

function handleResponses() {
  const lines = responseBuffer.split("\n");
  responseBuffer = lines.pop();
  
  for (const line of lines) {
    if (!line.trim()) continue;
    try {
      const response = JSON.parse(line);
      console.log(`Received Response for JSON-RPC ID: ${response.id}`);
      
      if (response.id === 1) {
        // Envoie initialized et tool/call
        sendNext(); // Send initialized
        setTimeout(sendNext, 500); // Send tool call
      } else if (response.id === 2) {
        // Result of tool call
        console.log("\n=================== RESULT ===================");
        if (response.error) {
          console.error("Tool execution error:", response.error);
        } else {
          console.log(JSON.stringify(response.result, null, 2));
        }
        console.log("==============================================");
        sendNext();
      }
    } catch (e) {
      console.log("Raw MCP output (could not parse as JSON):", line);
    }
  }
}
