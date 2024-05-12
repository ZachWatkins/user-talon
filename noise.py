from talon import Context, actions, speech_system

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
        print("popped during command")
        actions.user.dictation_mode(),

    def noise_trigger_hiss():
        print("hissed during command")
        speech_system.engine_mimic("go to sleep")

@dictation_ctx.action_class("user")
class UserActions:
    def noise_trigger_pop():
        print("popped during dictation")
        actions.user.command_mode()
