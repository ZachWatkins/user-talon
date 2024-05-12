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
        actions.key("t")
        actions.sleep("200ms")
        actions.insert(text)
        actions.key("enter")
        actions.sleep("100ms")

    def clickup_task_assign_to_me():
        actions.key("/")
        actions.sleep("100ms")
        actions.insert("Assign to me")
        actions.sleep("100ms")
        actions.key("enter")
        actions.sleep("100ms")

    def clickup_task_assign_to(name: str):
        actions.key("/")
        actions.sleep("100ms")
        actions.insert("assign")
        actions.key("enter")
        actions.sleep("100ms")
        actions.insert(name)
        actions.sleep("100ms")
        actions.key("enter")
        actions.sleep("100ms")

    def clickup_task_set_status(status: str):
        actions.key("/")
        actions.sleep("100ms")
        actions.insert("status")
        actions.key("space")
        actions.sleep("100ms")
        actions.insert(status)
        actions.key("space")
        actions.sleep("100ms")

    def clickup_task_set_priority(priority: str):
        actions.key("/")
        actions.sleep("100ms")
        actions.insert(f"{priority} Priority")
        actions.key("space")
        actions.sleep("100ms")

    def clickup_task_start_now():
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
        task_url = actions.clip.text()
        task_id = task_url.split("/")[-1]
        task_name_in_branch = re.sub(r"[^a-zA-Z0-9]", "", task_name.replace(" ", "_"))
        return f"ClickUp-{task_id}_{task_name_in_branch}"

    def clickup_task_create_from_selection(formatters: str) -> str:
        """Create task from selection."""
        selected = edit.selected_text()
        if not selected:
            app.notify("Asked to create task from selection, but nothing selected!")
            return
        # Open Chrome and navigate to ClickUp.
        user.switcher_focus("Google Chrome")
        actions.browser.focus_address()
        actions.insert("https://app.clickup.com/")
        actions.key("enter")
        actions.sleep("500ms")
        return selected
