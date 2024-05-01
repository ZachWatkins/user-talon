# For this to work, you need to have the ClickUp hotkeys setting enabled.
# To enable hotkeys:
# 1. In the upper-right corner, click your account avatar and select Settings.
# 2. Scroll down to the Preferences section.
# 3. Click Hotkeys on.
# 4. Click *Save changes*.
# https://help.clickup.com/hc/en-us/articles/6309030550167-Use-hotkeys-and-keyboard-shortcuts
mode: command
-

# Use the selected text as the name of the task.
^clickup task$:
    task_name = user.clickup_task_create_from_selection()
    user.clickup_task_create(task_name)
    user.clickup_task_assign_to_me()
    user.clickup_task_set_status("In Progress")
    user.clickup_task_set_priority("Normal")
    user.clickup_task_start_now()
    user.clickup_task_submit()
    key(3) # Copy the URL of the task, which includes the task ID at the end of the URL.
    sleep(100ms) # The task ID is now in the clipboard.
    # Generate a GitHub branch name using the task ID and the name of the task. The name of the task should only contain alphanumeric characters, and all spaces should be replaced with underscores.
    git_branch_name = user.clickup_get_git_branch_name(task_name)
    # Create a new branch in the current repository with the generated branch name.
    user.switcher_focus("Visual Studio Code")
    user.vscode("git.checkout")
    sleep(50ms)
    insert(git_branch_name)
