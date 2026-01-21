import * as vscode from 'vscode';
import axios from 'axios';

export async function ask() {
  const q = await vscode.window.showInputBox();
  if (!q) return;

  const res = await axios.post('http://localhost:8000/query/', {
    question: q
  });

  vscode.window.showInformationMessage(res.data.answer);
}
