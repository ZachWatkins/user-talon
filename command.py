from talon import Context, Module, actions, app

ctx = Context()
mod = Module()

ctx.matches = r"""
mode: command
"""

@mod.action_class
class Actions:
    def switch_apps():
        """Switch to the previous app"""
        if app.platform == "mac":
            actions.key("cmd-tab")
        else:
            actions.key("alt-tab")
