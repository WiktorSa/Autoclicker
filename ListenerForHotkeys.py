from pynput import keyboard


class ListenerForHotkeys:
    def __init__(self, app):
        self.app = app
        self.turn_on_hotkey = "ctrl_l + f2"
        self.turn_off_hotkey = "ctrl_l + f3"
        self.input = ""
        self.last_press = ""
        self.should_listen_for_turn_on_hotkey = True
        #  There is an error while typing ctrl+a for instance (a is not visible)
        #  If the user presses either ctrl_l or ctrl_r this number will increase to 1
        #  Than on_press will unpress this button and on_release will get notified of it and do nothing
        #  to avoid any possible consequences of doing that
        self.fix_against_ctrl_l = 0
        self.fix_against_ctrl_r = 0
        # Our listener that we will turn on and off while the program works
        self.listener = ""

    def start_listening(self):
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def stop_listening(self):
        self.listener.stop()

    def on_press(self, key):
        try:
            format_key = key.char
        except AttributeError:
            format_key = format(key)
            format_key = format_key[4:]

        if format_key != self.last_press:
            self.last_press = format_key
            if self.input != "":
                self.input = self.input + " + "

            self.input = self.input + str(format_key)

            if key == keyboard.Key.ctrl_l:
                self.fix_against_ctrl_l = 1
                keyboard.Controller().release(keyboard.Key.ctrl_l)

            if key == keyboard.Key.ctrl_r:
                self.fix_against_ctrl_r = 1
                keyboard.Controller().release(keyboard.Key.ctrl_r)

    def on_release(self, key):
        if key == keyboard.Key.ctrl_l and self.fix_against_ctrl_l == 1:
            pass
        elif key == keyboard.Key.ctrl_r and self.fix_against_ctrl_r == 1:
            pass
        else:
            if self.input == self.turn_on_hotkey and self.should_listen_for_turn_on_hotkey:
                self.app.start_autoclicker()

            #  We only listen for one of the given hotkeys (so that the user can use the same hotkey
            #  to start and end the autoclicker)
            if self.input == self.turn_off_hotkey and not self.should_listen_for_turn_on_hotkey:
                self.app.stop_autoclicker()

            self.last_press = ""
            self.input = ""
            self.fix_against_ctrl_l = 0
            self.fix_against_ctrl_r = 0

    def change_hotkeys(self, hotkey, is_it_turn_on_hotkey):
        if is_it_turn_on_hotkey:
            self.turn_on_hotkey = hotkey
        else:
            self.turn_off_hotkey = hotkey

    def change_listen_for_turn_on_hotkey(self, state):
        self.should_listen_for_turn_on_hotkey = state
