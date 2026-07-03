import re
from talon import Context, Module, actions, app, clip

ctx = Context()
mod = Module()

ctx.matches = r"""
tag: browser
browser.host: app.clickup.com
"""

@mod.action_class
class Actions:
    def clickup_task_submit():
        """Press the specified key with the correct modifier key for the OS"""
        if app.platform == "mac":
            actions.key("cmd-enter")
        else:
            actions.key("ctrl-enter")
        actions.sleep("800ms")

    def clickup_task_create(task_name: str) -> str:
        """Create a task with the specified text"""
        actions.key("t")
        actions.sleep("500ms")
        if not task_name:
            app.notify("Task name is missing!")
            return ""
        actions.insert(task_name)
        actions.sleep("100ms")
        actions.key("tab")
        actions.sleep("500ms")
        actions.user.clickup_task_assign_to_me()
        actions.user.clickup_task_set_status("Progress")
        actions.user.clickup_task_set_priority("Normal")
        actions.user.clickup_task_start_now()
        actions.user.clickup_task_submit()
        # Pin to bottom of window.
        actions.key("1")
        actions.sleep("100ms")
        # Copy the URL of the task, which includes the task ID at the end of the URL.
        actions.key("2")
        actions.sleep("100ms")
        task_url = clip.text()
        # View the task.
        actions.key("3")
        actions.sleep("100ms")
        return task_url

    def github_branch_issue_create(task_name: str, task_url: str):
        """Create a new branch and issue in the current repository with the name of the task and a link to the task in ClickUp."""
        if not task_name:
            app.notify("Task name is missing!")
            return
        if not task_url:
            app.notify("Task URL is missing!")
            return
        # Generate a GitHub issue and branch using the task ID and the name of the task.
        command = f"gh issue create --title \"{task_name}\" --body \"ClickUp task: {task_url}\" --assignee \"@me\""
        actions.insert(command)
        actions.key("enter")
        actions.sleep("6000ms")
        # Get the last line of the terminal output which is the URL of the issue.
        actions.user.vscode("workbench.action.terminal.copyLastCommandOutput")
        actions.sleep("100ms")
        last_output = clip.text()
        issue_id = last_output.split("/")[-1].strip()
        issue_id_only_numbers = re.sub(r"\D", "", issue_id)
        # If the lengths differ, then the issue ID was not selected correctly. Alert the user and return.
        if len(issue_id) != len(issue_id_only_numbers):
            print(f"Issue ID is not a number: {issue_id}, only numbers: {issue_id_only_numbers}")
            app.notify("Issue ID is not a number! Please check the terminal output.")
            return
        # Get the current branch name from the terminal, since this can be different between repositories.
        command = f"git rev-parse --abbrev-ref HEAD"
        actions.insert(command)
        actions.key("enter")
        actions.sleep("1000ms")
        actions.user.vscode("workbench.action.terminal.copyLastCommandOutput")
        actions.sleep("100ms")
        current_branch_name = clip.text().strip()
        # Create a branch for the issue.
        git_branch_name = actions.user.clickup_get_git_branch_name(task_name, task_url)
        command = f"gh issue develop {issue_id} --name {git_branch_name} --base {current_branch_name}"
        actions.insert(command)
        actions.key("enter")
        actions.sleep("6000ms")
        actions.user.vscode("workbench.action.terminal.kill")

    def clickup_task_assign_to_me():
        """Assign the task to the current user"""
        actions.key("/")
        actions.sleep("100ms")
        actions.insert("Assign to me")
        actions.sleep("100ms")
        actions.key("enter")
        actions.sleep("100ms")

    def clickup_task_set_status(status: str):
        """Set the status of the task"""
        actions.key("/")
        actions.sleep("100ms")
        actions.insert("status")
        actions.key("space")
        actions.sleep("100ms")
        actions.insert(status)
        actions.key("space")
        actions.sleep("100ms")

    def clickup_task_set_priority(priority: str):
        """Set the priority of the task"""
        actions.key("/")
        actions.sleep("100ms")
        actions.insert(f"{priority} Priority")
        actions.key("space")
        actions.sleep("100ms")

    def clickup_task_start_now():
        """Set the start date of the task to now"""
        actions.key("/")
        actions.sleep("100ms")
        actions.insert("start date")
        actions.key("space")
        actions.sleep("100ms")
        actions.insert("now")
        actions.sleep("1000ms")
        actions.key("enter")
        actions.sleep("100ms")

    def clickup_get_git_branch_name(task_name: str, task_url: str) -> str:
        """Get the git branch name from the task name"""
        task_id = task_url.split("/")[-1]
        task_name_in_branch = re.sub(r"[^a-zA-Z0-9_]", "", task_name.replace(" ", "_"))
        return f"ClickUp-{task_id}_{task_name_in_branch}"

    def clickup_add_issue_to_clipboard(task_name: str, task_url: str):
        """Add the issue to the clipboard."""
        # Format:
        # <task_name>
        #
        # Assignees: @ZachWatkins
        #
        # ClickUp task: <task_url>
        if not task_name or not task_url:
            app.notify("Task name or URL is missing!")
            return
        issue_text = f"{task_name}\n\nAssignees: @ZachWatkins\n\nClickUp task: {task_url}"
        clip.set(issue_text)
