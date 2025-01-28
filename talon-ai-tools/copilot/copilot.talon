app: vscode
not tag: user.codeium
-
clippy jest: user.vscode("editor.action.inlineSuggest.trigger")
clippy next: user.vscode("editor.action.inlineSuggest.showNext")
clippy (previous | last): user.vscode("editor.action.inlineSuggest.showPrevious")
clippy yes: user.vscode("editor.action.inlineSuggest.commit")
clippy yes word: user.vscode("editor.action.inlineSuggest.acceptNextWord")
clippy nope: user.vscode("editor.action.inlineSuggest.undo")
clippy cancel: user.vscode("editor.action.inlineSuggest.hide")
clippy block last: user.vscode("workbench.action.chat.previousCodeBlock")
clippy block next: user.vscode("workbench.action.chat.nextCodeBlock")
clippy new file <user.ordinal_or_last>:
    user.copilot_focus_code_block(ordinal_or_last)
    user.vscode("workbench.action.chat.insertIntoNewFile")
clippy copy <user.ordinal_or_last>:
    user.copilot_focus_code_block(ordinal_or_last)
    edit.copy()
clippy bring <user.ordinal_or_last>: user.copilot_bring_code_block(ordinal_or_last)
clippy bring <user.ordinal_or_last> {user.makeshift_destination} <user.cursorless_target>:
    user.cursorless_command(makeshift_destination, cursorless_target)
    user.copilot_bring_code_block(ordinal_or_last)
clippy chat [<user.prose>]$: user.copilot_chat(prose or "")
clippy {user.copilot_slash_command} <user.cursorless_target> [to <user.prose>]$:
    user.cursorless_command("setSelection", cursorless_target)
    user.copilot_inline_chat(copilot_slash_command or "", prose or "")
clippy make [<user.prose>]: user.copilot_inline_chat("", prose or "")
