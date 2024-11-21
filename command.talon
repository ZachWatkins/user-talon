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

### direction keys ###
up: key(up)
down: key(down)
left: key(left)
right: key(right)
next slide: key(right)
last slide: key(left)

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

mouse off: user.mouse_sleep()
mouse on: user.mouse_wake()

### Screencasting ###
grab that: user.screen_record()
grab cameras: user.screencast_start()

key(^:down): user.switch_to_dictation_mode()
