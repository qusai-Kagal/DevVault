import * as vscode from 'vscode';
import ollama from 'ollama';

export function activate(context: vscode.ExtensionContext) {
    console.log('Activating Deep-Seeker extension');
    const disposable = vscode.commands.registerCommand('deep-seeker-ext.start', () => {
        console.log('Command deep-seeker-ext.start executed');
        const panel = vscode.window.createWebviewPanel(
            'deepChat',
            'Deep Seek Chat',
            vscode.ViewColumn.One,
            { enableScripts: true }
        );

        panel.webview.html = getWebviewContent();
        console.log('Webview content set');

        panel.webview.onDidReceiveMessage(async (message: any) => {
            console.log('Received message from webview:', message);
            const userPrompt = message.text;
            let responseText = '';

            try {
                const streamResponse = await ollama.chat({
                    model: 'deepseek-r1:7b',
                    messages: [{ role: 'user', content: userPrompt }],
                    stream: true
                });
                console.log('Received stream response');
                for await (const part of streamResponse) {
                    responseText += part.message.content;
                    panel.webview.postMessage({ command: 'response', text: responseText });
                    console.log('Sent response to webview:', responseText);
                }
            } catch (err) {
                console.error('Error during chat:', err);
                panel.webview.postMessage({ command: 'chatResponse', text: `Error: ${String(err)}` });
            }
        });
        context.subscriptions.push(disposable);
    });
}

function getWebviewContent(): string {
    return /*html*/`
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <style>
        body { font-family: Arial, sans-serif; margin: 1rem; background-color: #f4f4f9; color: #333; }
        h2 { color: #007acc; }
        #prompt { width: 100%; box-sizing: border-box; padding: 0.5rem; margin-bottom: 1rem; border: 1px solid #ccc; border-radius: 4px; }
        #askBtn { background-color: #007acc; color: white; border: none; padding: 0.5rem 1rem; border-radius: 4px; cursor: pointer; }
        #askBtn:hover { background-color: #005f99; }
        #response { border: 1px solid #ccc; padding: 0.5rem; margin-top: 1rem; border-radius: 4px; background-color: white; }
    </style>
    </head>
    <body>
    <h2>Deep Seek Chat</h2>
    <textarea id="prompt" rows="5" placeholder="Ask a question..."></textarea><br />
    <button id="askBtn">Ask</button>
    <div id="response"></div>
    <script>
        const vscode = acquireVsCodeApi();
        console.log('Webview script loaded');

        document.getElementById('askBtn').addEventListener('click', () => {
            const text = document.getElementById('prompt').value;
            console.log('Ask button clicked, sending message to extension:', text);
            vscode.postMessage({ command: 'chat', text });
        });

        window.addEventListener('message', event => {
            const { command, text } = event.data;
            console.log('Received message from extension:', event.data);
            if (command === 'response' || command === 'chatResponse') {
                document.getElementById('response').innerText = text;
            }
        });
    </script>
    </body>
    </html>
    `;
}

export function deactivate() {
    console.log('Deactivating Deep-Seeker extension');
}
