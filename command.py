from talon import Context, Module, actions, app

ctx = Context()
mod = Module()

ctx.matches = r"""
mode: command
"""

@mod.action_class
class Actions:
    def switch_to_dictation_mode():
        """Switch from command to dictation mode"""
        print("switching to dictation mode")
        app.notify(title="Dictation mode",
                   subtitle="On",
                   sound=True)
        actions.mode.disable("sleep")
        actions.mode.disable("command")
        actions.mode.enable("dictation")
        actions.user.code_clear_language_mode()
        actions.user.gdb_disable()

    def switch_apps():
        """Switch to the previous app"""
        if app.platform == "mac":
            actions.key("cmd-tab")
        else:
            actions.key("alt-tab")

    def screencast_start():
        """Start a screencast"""
        if app.platform == "mac":
            path = "quicktime"
            ui.launch(path=path)
        elif app.platform == "windows":
            path = "clipchamp"
            is_valid_path = False
            try:
                current_path = Path(path)
                is_valid_path = current_path.is_file()
            except:
                is_valid_path = False
            if is_valid_path:
                ui.launch(path=path)
            else:
                cmd = f"explorer.exe shell:AppsFolder\\{path}"
                subprocess.Popen(cmd, shell=False)
        else:
            print("Unhandled platform in screencast_start: " + app.platform)

    def screen_record():
        """Record the screen"""
        if app.platform == "mac":
            actions.key("super-shift-5")
            rect = ui.active_window().rect
            ctrl.mouse_move(rect.left + (rect.width / 2), rect.top + (rect.height / 2))
        elif app.platform == "windows":
            # actions.key("super-shift-r"); rect = ui.main_screen().rect; previous_position = ctrl.mouse_pos(); ctrl.mouse_move(0, 0); actions.sleep("750ms"); ctrl.mouse_click(button=0, down=True); ctrl.mouse_move(rect.width, rect.height); ctrl.mouse_click(button=0, up=True); actions.sleep("50ms"); ctrl.mouse_move((rect.width / 2) - 135, 48); actions.sleep("500ms"); ctrl.mouse_move((rect.width / 2) - 140, 48); actions.sleep("50ms"); ctrl.mouse_click(button=0, down=True); actions.sleep("50ms"); ctrl.mouse_click(button=0, down=True); actions.sleep("500ms"); ctrl.mouse_click(button=0, up=True);
            actions.key("super-shift-r")
            actions.key("super-shift-r")
            rect = ui.main_screen().rect
            previous_position = ctrl.mouse_pos()
            ctrl.mouse_move(0, 0)
            actions.sleep("750ms")
            ctrl.mouse_click(button=0, down=True)
            ctrl.mouse_move(rect.width, rect.height)
            ctrl.mouse_click(button=0, up=True)
            actions.sleep("50ms")
            ctrl.mouse_move((rect.width / 2) - 135, 48)
            actions.sleep("500ms")
            ctrl.mouse_move((rect.width / 2) - 140, 48)
            actions.sleep("50ms")
            ctrl.mouse_click(button=0, down=True)
            actions.sleep("50ms")
            ctrl.mouse_click(button=0, down=True)
            actions.sleep("500ms")
            ctrl.mouse_click(button=0, up=True)
        else:
            print("Unhandled platform in screen_record: " + app.platform)
