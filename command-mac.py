from talon import Context, Module, actions

ctx = Context()
mod = Module()

ctx.matches = r"""
mode: command
"""

@mod.action_class
class Actions:
    def macos_run_shortcut(name: str):
        """Runs a macOS Shortcut by its exact name."""
        # subprocess.Popen(["shortcuts", "run", name])
        actions.user.system_command(f"shortcuts run '{name}'")
