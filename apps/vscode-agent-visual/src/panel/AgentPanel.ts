import * as vscode from 'vscode';
import { AgentStateManager } from '../state/AgentStateManager';
import { getWebviewContent } from '../utils/webview-helpers';

export class AgentPanel {
  public static currentPanel: AgentPanel | undefined;
  private static readonly viewType = 'agentVisual.panel';
  private readonly _panel: vscode.WebviewPanel;
  private _disposables: vscode.Disposable[] = [];

  public static createOrShow(
    context: vscode.ExtensionContext,
    stateManager: AgentStateManager
  ) {
    const column = vscode.window.activeTextEditor
      ? vscode.window.activeTextEditor.viewColumn
      : undefined;

    if (AgentPanel.currentPanel) {
      AgentPanel.currentPanel._panel.reveal(column);
      return;
    }

    const panel = vscode.window.createWebviewPanel(
      AgentPanel.viewType,
      'Agent Visual — Mode Etendu',
      column || vscode.ViewColumn.One,
      {
        enableScripts: true,
        localResourceRoots: [
          vscode.Uri.joinPath(context.extensionUri, 'media'),
          vscode.Uri.joinPath(context.extensionUri, 'dist')
        ],
        retainContextWhenHidden: false
      }
    );

    AgentPanel.currentPanel = new AgentPanel(panel, context, stateManager);
  }

  private constructor(
    panel: vscode.WebviewPanel,
    context: vscode.ExtensionContext,
    private readonly _stateManager: AgentStateManager
  ) {
    this._panel = panel;

    this._panel.webview.html = getWebviewContent(
      this._panel.webview,
      context.extensionUri,
      'panel'
    );

    const stateListener = this._stateManager.onDidChangeState((state) => {
      this._panel.webview.postMessage({
        type: 'state:update',
        payload: state
      });
    });
    this._disposables.push(stateListener);

    this._panel.webview.onDidReceiveMessage(
      (message) => this._handleMessage(message),
      undefined,
      this._disposables
    );

    this._panel.onDidDispose(() => this.dispose(), null, this._disposables);
  }

  private async _handleMessage(message: { type: string; payload?: unknown }) {
    const allowedTypes = ['chat:send', 'avatar:request', 'animation:control', 'ui:ready'];
    if (!allowedTypes.includes(message.type)) {
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
          this._panel.webview.postMessage({
            type: 'chat:response',
            payload: { text: response, emotion: 'happy' }
          });
        } catch (err) {
          this._panel.webview.postMessage({
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
        this._panel.webview.postMessage({
          type: 'state:init',
          payload: this._stateManager.getState()
        });
        break;
      }
    }
  }

  public dispose() {
    AgentPanel.currentPanel = undefined;
    this._panel.dispose();
    while (this._disposables.length) {
      const d = this._disposables.pop();
      d?.dispose();
    }
  }
}
