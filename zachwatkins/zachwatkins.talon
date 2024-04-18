# custom commands go here
app: vscode
-
hey code [<user.text>]:
    user.vscode("workbench.action.openQuickChat.copilot")
    insert(user.text or "")

hello code [<user.text>]:
    user.vscode("workbench.action.openChat.copilot")
    insert(user.text or "")

rerun: user.vscode("workbench.action.terminal.runRecentCommand")
