# custom commands go here
app: vscode
-
hey code [<user.text>]:
    user.vscode("workbench.action.openQuickChat.copilot")
    insert(user.text or "")

hello code [<user.text>]:
    user.vscode("workbench.action.openChat.copilot")!
    insert(user.text or "")

rerun: user.vscode("workbench.action.terminal.runRecentCommand")

artisan test: user.run_rpc_command("workbench.action.tasks.runTask", "Laravel: Test")

docker up: "docker-compose up -d\n"
docker down: "docker-compose down\n"