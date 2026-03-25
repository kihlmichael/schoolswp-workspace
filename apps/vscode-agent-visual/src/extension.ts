import * as vscode from 'vscode';
import { AgentSidebarProvider } from './sidebar/AgentSidebarProvider';
import { AgentPanel } from './panel/AgentPanel';
import { AgentStateManager } from './state/AgentStateManager';

export function activate(context: vscode.ExtensionContext) {
  const stateManager = new AgentStateManager(context);
  const sidebarProvider = new AgentSidebarProvider(context, stateManager);

  // Register sidebar webview
  context.subscriptions.push(
    vscode.window.registerWebviewViewProvider(
      'agentVisual.sidebar',
      sidebarProvider,
      { webviewOptions: { retainContextWhenHidden: false } }
    )
  );

  // Commands
  context.subscriptions.push(
    vscode.commands.registerCommand('agentVisual.start', () => {
      stateManager.setRunning(true);
    }),
    vscode.commands.registerCommand('agentVisual.stop', () => {
      stateManager.setRunning(false);
    }),
    vscode.commands.registerCommand('agentVisual.pause', () => {
      stateManager.togglePause();
    }),
    vscode.commands.registerCommand('agentVisual.changeAvatar', async () => {
      const avatars = stateManager.getAvailableAvatars();
      const picked = await vscode.window.showQuickPick(avatars, {
        placeHolder: 'Choisir un avatar'
      });
      if (picked) {
        stateManager.setAvatar(picked);
      }
    }),
    vscode.commands.registerCommand('agentVisual.setSpeed', async () => {
      const speed = await vscode.window.showQuickPick(
        ['0.5x', '1x', '1.5x', '2x'],
        { placeHolder: 'Vitesse d\'animation' }
      );
      if (speed) {
        stateManager.setSpeed(parseFloat(speed));
      }
    }),
    vscode.commands.registerCommand('agentVisual.toggleFocus', () => {
      stateManager.toggleFocusMode();
    }),
    vscode.commands.registerCommand('agentVisual.openPanel', () => {
      AgentPanel.createOrShow(context, stateManager);
    })
  );

  // Check Workspace Trust
  if (!vscode.workspace.isTrusted) {
    vscode.window.showWarningMessage(
      'Agent Visual: certaines fonctionnalites sont desactivees en mode restreint.'
    );
    stateManager.setRestrictedMode(true);
  }

  context.subscriptions.push(
    vscode.workspace.onDidGrantWorkspaceTrust(() => {
      stateManager.setRestrictedMode(false);
    })
  );
}

export function deactivate() {
  // Cleanup is handled by disposables in context.subscriptions
}
