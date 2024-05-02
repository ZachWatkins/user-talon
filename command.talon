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
