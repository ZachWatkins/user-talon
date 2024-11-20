from talon import Context, Module, actions, app

ctx = Context()
mod = Module()

ctx.matches = r"""
mode: dictation
"""

@mod.action_class
class Actions:
    def switch_to_command_mode():
        """Switch from dictation to command mode"""
        print("switching to command mode")
        app.notify(title="Command mode",
                   subtitle="On",
                   sound=True)
        actions.mode.disable("sleep")
        actions.mode.disable("dictation")
        actions.mode.enable("command")
        actions.user.code_clear_language_mode()
        actions.user.gdb_disable()
