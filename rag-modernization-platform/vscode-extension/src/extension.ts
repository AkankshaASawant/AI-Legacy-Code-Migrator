import * as vscode from 'vscode';
import { ask } from './commands/ask';

export function activate(context: vscode.ExtensionContext) {
  context.subscriptions.push(
    vscode.commands.registerCommand('rag.ask', ask)
  );
}
