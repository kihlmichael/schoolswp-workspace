import { spawn } from 'child_process';
import * as vscode from 'vscode';

export class ClaudeCLI {
  private _claudePath: string;

  constructor() {
    this._claudePath = 'claude';
  }

  /**
   * Send a prompt to Claude Code CLI and get the response.
   * Uses `claude -p` for non-interactive single-prompt mode.
   */
  public async send(prompt: string): Promise<string> {
    return new Promise((resolve, reject) => {
      const args = ['-p', prompt, '--output-format', 'text'];

      const proc = spawn(this._claudePath, args, {
        cwd: vscode.workspace.workspaceFolders?.[0]?.uri.fsPath,
        env: { ...process.env },
        shell: true,
        timeout: 120_000
      });

      let stdout = '';
      let stderr = '';

      proc.stdout.on('data', (data: Buffer) => {
        stdout += data.toString();
      });

      proc.stderr.on('data', (data: Buffer) => {
        stderr += data.toString();
      });

      proc.on('close', (code) => {
        if (code === 0) {
          resolve(stdout.trim());
        } else {
          reject(new Error(`Claude CLI exited with code ${code}: ${stderr}`));
        }
      });

      proc.on('error', (err) => {
        reject(new Error(`Failed to spawn Claude CLI: ${err.message}`));
      });
    });
  }

  /**
   * Send a prompt with streaming output (for progressive display).
   */
  public async sendStreaming(
    prompt: string,
    onChunk: (text: string) => void
  ): Promise<string> {
    return new Promise((resolve, reject) => {
      const args = ['-p', prompt, '--output-format', 'stream-json'];

      const proc = spawn(this._claudePath, args, {
        cwd: vscode.workspace.workspaceFolders?.[0]?.uri.fsPath,
        env: { ...process.env },
        shell: true,
        timeout: 120_000
      });

      let fullResponse = '';
      let buffer = '';

      proc.stdout.on('data', (data: Buffer) => {
        buffer += data.toString();
        const lines = buffer.split('\n');
        buffer = lines.pop() || '';

        for (const line of lines) {
          if (!line.trim()) { continue; }
          try {
            const parsed = JSON.parse(line);
            if (parsed.type === 'assistant' && parsed.message?.content) {
              for (const block of parsed.message.content) {
                if (block.type === 'text') {
                  onChunk(block.text);
                  fullResponse += block.text;
                }
              }
            }
          } catch {
            onChunk(line);
            fullResponse += line;
          }
        }
      });

      proc.on('close', (code) => {
        if (code === 0) {
          resolve(fullResponse);
        } else {
          reject(new Error(`Claude CLI streaming error (code ${code})`));
        }
      });

      proc.on('error', (err) => {
        reject(new Error(`Failed to spawn Claude CLI: ${err.message}`));
      });
    });
  }

  /**
   * Check if Claude CLI is available.
   */
  public async isAvailable(): Promise<boolean> {
    return new Promise((resolve) => {
      const proc = spawn(this._claudePath, ['--version'], {
        shell: true,
        timeout: 5000
      });
      proc.on('close', (code) => resolve(code === 0));
      proc.on('error', () => resolve(false));
    });
  }
}
