mode: command
-

# When people say good morning to me, I want to be able to respond without triggering anything.
^morning$: sleep(5ms)
^hey$: sleep(5ms)
^howdy$: sleep(5ms)

# Talon frequently misinterprets these commands, likely due to microphone noise.
^pit bat$: edit.paste() # "paste that"
^paste at$: edit.paste() # "paste that"
^(ta | tap)$: key(tab) # "tab"

### text navigation ###
up: key(up)
down: key(down)
left: key(left)
right: key(right)

### text manipulation ###
drop: key(backspace)
dropper: key(backspace:2)

### quick text ###
thumbs up: insert('👍')

^switch [<phrase>]$: user.switch_apps()
