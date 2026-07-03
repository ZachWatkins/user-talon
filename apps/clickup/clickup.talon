# For this to work, you need to have the ClickUp Keyboard Shortcuts setting enabled.
# To enable Keyboard Shortcuts:
# 1. In the upper-right corner, click your account avatar and select Settings.
# 2. Scroll down to the Preferences section.
# 3. Toggle Keyboard Shortcuts on.
# 4. Click *Save changes*.
# https://help.clickup.com/hc/en-us/articles/6309030550167-Use-keyboard-shortcuts
mode: command
-

# Use the selected text as the name of the task.
^clickup task$:
    mode.disable("command")
    task_name = edit.selected_text()
    sleep(100ms)
    user.switcher_focus("Google Chrome")
    sleep(100ms)
    key("cmd-3")
    sleep(500ms)
    task_url = user.clickup_task_create(task_name)
    user.github_branch_issue_create(task_name, task_url)
    mode.enable("command")
