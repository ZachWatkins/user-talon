from talon import Context, actions, app, speech_system

command_ctx = Context()
command_ctx.matches = r"""
mode: command
os: mac
"""

dictation_ctx = Context()
dictation_ctx.matches = r"""
mode: dictation
os: mac
"""

@command_ctx.action_class("user")
class UserActions:
    def noise_trigger_pop():
        """Enable dictation mode"""
        print("popped during command")
        app.notify(title="Dictation mode",
                   subtitle="On",
                   sound=True)
        actions.mode.disable("sleep")
        actions.mode.disable("command")
        actions.mode.enable("dictation")
        actions.user.code_clear_language_mode()
        actions.user.gdb_disable(),

    # def noise_trigger_hiss(active: bool):
    #     print("hissed during command")
    #     speech_system.engine_mimic("go to sleep")

@dictation_ctx.action_class("user")
class UserActions:
    def noise_trigger_pop():
        """Enable command mode"""
        print("popped during dictation")
        app.notify(title="Command mode",
                   subtitle="On",
                   sound=True)
        actions.mode.disable("sleep")
        actions.mode.disable("dictation")
        actions.mode.enable("command")
