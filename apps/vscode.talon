# custom commands go here
app: vscode
-
hey code [<user.text>]:
    user.vscode("workbench.action.openQuickChat.copilot")
    insert(user.text or "")

hello code [<user.text>]:
    user.vscode("workbench.action.openChat.copilot")!
    insert(user.text or "")

again: user.vscode("workbench.action.terminal.runRecentCommand")

artisan test: user.run_rpc_command("workbench.action.tasks.runTask", "Laravel: Test")

docker up: "docker-compose up -d\n"
docker down: "docker-compose down\n"
node run: insert('npm run ')

point: key(- >)
pointer: key(space = > space)
assign:
    insert(' = ;')
    key(left)
assign string:
    insert(' = "";')
    key(left:2)
assign array:
    insert(' = [];')
    key(left:2)
assign object:
    insert(' = {};')
    key(left:2)
assign function:
    insert(' = function(){};')
    key(left:4)
assign arrow function:
    insert(' = () => {};')
    key(left:4)
array:
    insert('[];')
    key(left:2)
object:
    insert('{};')
    key(left:2)
function: insert('function ')
nolan: insert('null')
this dot: insert('this.')
console log:
    insert('console.log();')
    key(left:2)
console error:
    insert('console.error();')
    key(left:2)
process exit:
    insert('process.exit();')
    key(left:2)
equals: insert(' === ')
not equals: insert(' !== ')

code import:
    insert('import {  } from ;')
    key(left)
    key('"')
export: insert('export ')
export default: insert('expert default ')
constant: insert('const ')
lettuce: insert('let ')
code return:
    insert('return;')
    key(left)

# php
public: insert('public ')
protected: insert('protected ')
private: insert('private ')
elephant:
    insert('<?php  ?>')
    key(left:3)
for each:
    insert('foreach ('))
    key('$')
