import * as vscode from 'vscode';
import { ClaudeCLI } from '../bridge/ClaudeCLI';

interface AgentState {
  running: boolean;
  paused: boolean;
  avatar: string;
  speed: number;
  focusMode: boolean;
  chatLoading: boolean;
  restrictedMode: boolean;
  lastActivity?: { type: string; detail?: string };
}

export class AgentStateManager {
  private _state: AgentState;
  private _onDidChangeState = new vscode.EventEmitter<AgentState>();
  public readonly onDidChangeState = this._onDidChangeState.event;
  private _claudeBridge: ClaudeCLI;

  constructor(private readonly _context: vscode.ExtensionContext) {
    const config = vscode.workspace.getConfiguration('agentVisual');
    this._state = {
      running: true,
      paused: false,
      avatar: config.get<string>('defaultAvatar', 'robot-default'),
      speed: config.get<number>('animationSpeed', 1),
      focusMode: false,
      chatLoading: false,
      restrictedMode: false
    };
    this._claudeBridge = new ClaudeCLI();
  }

  public getState(): AgentState {
    return { ...this._state };
  }

  public getAvailableAvatars(): string[] {
    return ['robot-default', 'robot-blue', 'cat-orange', 'ghost-pixel'];
  }

  public setRunning(running: boolean) {
    this._state.running = running;
    this._emit();
  }

  public togglePause() {
    this._state.paused = !this._state.paused;
    this._emit();
  }

  public setAvatar(avatar: string) {
    this._state.avatar = avatar;
    this._emit();
  }

  public setSpeed(speed: number) {
    this._state.speed = Math.max(0.5, Math.min(2, speed));
    this._emit();
  }

  public toggleFocusMode() {
    this._state.focusMode = !this._state.focusMode;
    this._emit();
  }

  public setChatLoading(loading: boolean) {
    this._state.chatLoading = loading;
    this._emit();
  }

  public setRestrictedMode(restricted: boolean) {
    this._state.restrictedMode = restricted;
    this._emit();
  }

  public async sendToClaudeCode(prompt: string): Promise<string> {
    if (this._state.restrictedMode) {
      throw new Error('Claude Code integration desactivee en mode restreint');
    }
    return this._claudeBridge.send(prompt);
  }

  private _emit() {
    this._onDidChangeState.fire({ ...this._state });
  }
}
