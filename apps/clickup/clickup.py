import re
from talon import Context, Module, actions, app

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
        actions.sleep("1000ms")

    def clickup_task_create(text: str):
        """Create a task with the specified text"""
        actions.key("t")
        actions.sleep("500ms")
        actions.insert(text)
        actions.key("enter")
        actions.sleep("100ms")

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

    def clickup_get_git_branch_name(task_name: str):
        """Get the git branch name from the task name"""
        task_url = actions.clip.text()
        task_id = task_url.split("/")[-1]
        task_name_in_branch = re.sub(r"[^a-zA-Z0-9]", "", task_name.replace(" ", "_"))
        return f"ClickUp-{task_id}_{task_name_in_branch}"

    def get_selected_text() -> str:
        """Create task from selection."""
        selected = actions.edit.selected_text()
        if not selected:
            app.notify("No text selected!")
            return
        return selected
