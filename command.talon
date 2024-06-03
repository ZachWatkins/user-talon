mode: command
-

# When people say good morning to me, I want to be able to respond without triggering anything.
^morning$: sleep(5ms)
^hey$: sleep(5ms)
^howdy$: sleep(5ms)

# Talon frequently misinterprets these commands, likely due to microphone noise.
# "paste that"
^pit bat$: edit.paste()
^paste at$: edit.paste()
# "tab"
^(ta | tap)$: key(tab)

### text navigation ###
up: key(up)
down: key(down)
left: key(left)
right: key(right)

### text manipulation ###
^(drop | draw): key(backspace)
dropper: key(backspace:2)

### quick text ###
thumbs up: insert('👍')

^switch [<phrase>]$: user.switch_apps()

copy: edit.copy()
cut: edit.cut()
paste: edit.paste()
undo: edit.undo()
redo: edit.redo()
screenshot: key(cmd-shift-4)
