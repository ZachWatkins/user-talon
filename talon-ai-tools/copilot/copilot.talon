app: vscode
not tag: user.codeium
-
copilot jest: user.vscode("editor.action.inlineSuggest.trigger")
copilot next: user.vscode("editor.action.inlineSuggest.showNext")
copilot (previous | last): user.vscode("editor.action.inlineSuggest.showPrevious")
copilot yes: user.vscode("editor.action.inlineSuggest.commit")
copilot yes word: user.vscode("editor.action.inlineSuggest.acceptNextWord")
copilot nope: user.vscode("editor.action.inlineSuggest.undo")
copilot cancel: user.vscode("editor.action.inlineSuggest.hide")
copilot block last: user.vscode("workbench.action.chat.previousCodeBlock")
copilot block next: user.vscode("workbench.action.chat.nextCodeBlock")
copilot new file <user.ordinal_or_last>:
    user.copilot_focus_code_block(ordinal_or_last)
    user.vscode("workbench.action.chat.insertIntoNewFile")
copilot copy <user.ordinal_or_last>:
    user.copilot_focus_code_block(ordinal_or_last)
    edit.copy()
copilot bring <user.ordinal_or_last>: user.copilot_bring_code_block(ordinal_or_last)
copilot bring <user.ordinal_or_last> {user.makeshift_destination} <user.cursorless_target>:
    user.cursorless_command(makeshift_destination, cursorless_target)
    user.copilot_bring_code_block(ordinal_or_last)
copilot chat [<user.prose>]$: user.copilot_chat(prose or "")
copilot {user.copilot_slash_command} <user.cursorless_target> [to <user.prose>]$:
    user.cursorless_command("setSelection", cursorless_target)
    user.copilot_inline_chat(copilot_slash_command or "", prose or "")
copilot make [<user.prose>]: user.copilot_inline_chat("", prose or "")
