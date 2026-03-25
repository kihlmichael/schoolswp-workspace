import * as vscode from 'vscode';
import { AgentStateManager } from '../state/AgentStateManager';
import { getWebviewContent } from '../utils/webview-helpers';

export class AgentSidebarProvider implements vscode.WebviewViewProvider {
  public static readonly viewType = 'agentVisual.sidebar';
  private _view?: vscode.WebviewView;

  constructor(
    private readonly _context: vscode.ExtensionContext,
    private readonly _stateManager: AgentStateManager
  ) {
    this._stateManager.onDidChangeState((state) => {
      this._view?.webview.postMessage({
        type: 'state:update',
        payload: state
      });
    });
  }

  public resolveWebviewView(
    webviewView: vscode.WebviewView,
    _context: vscode.WebviewViewResolveContext,
    _token: vscode.CancellationToken
  ): void {
    this._view = webviewView;

    webviewView.webview.options = {
      enableScripts: true,
      localResourceRoots: [
        vscode.Uri.joinPath(this._context.extensionUri, 'media'),
        vscode.Uri.joinPath(this._context.extensionUri, 'dist')
      ]
    };

    webviewView.webview.html = getWebviewContent(
      webviewView.webview,
      this._context.extensionUri,
      'sidebar'
    );

    webviewView.webview.onDidReceiveMessage(
      (message) => this._handleMessage(message),
      undefined,
      []
    );

    webviewView.webview.postMessage({
      type: 'state:init',
      payload: this._stateManager.getState()
    });

    webviewView.onDidDispose(() => {
      this._view = undefined;
    });
  }

  private async _handleMessage(message: { type: string; payload?: unknown }) {
    const allowedTypes = ['chat:send', 'avatar:request', 'animation:control', 'ui:ready'];
    if (!allowedTypes.includes(message.type)) {
      console.warn(`[AgentVisual] Unknown message type: ${message.type}`);
      return;
    }

    switch (message.type) {
      case 'chat:send': {
        const text = message.payload as string;
        if (typeof text !== 'string' || text.length > 10000) {
          return;
        }
        this._stateManager.setChatLoading(true);
        try {
          const response = await this._stateManager.sendToClaudeCode(text);
          this._view?.webview.postMessage({
            type: 'chat:response',
            payload: { text: response, emotion: 'happy' }
          });
        } catch (err) {
          this._view?.webview.postMessage({
            type: 'chat:error',
            payload: { error: (err as Error).message }
          });
        } finally {
          this._stateManager.setChatLoading(false);
        }
        break;
      }
      case 'animation:control': {
        const action = message.payload as { action: string };
        if (action?.action === 'pause') {
          this._stateManager.togglePause();
        }
        break;
      }
      case 'ui:ready': {
        this._view?.webview.postMessage({
          type: 'state:init',
          payload: this._stateManager.getState()
        });
        break;
      }
    }
  }
}
