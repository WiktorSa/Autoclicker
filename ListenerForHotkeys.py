from pynput import keyboard

"""
Implement a simple algorithm that will check if the autoclicker works (you just need to include an extra
self.variable and a function to change it
"""


class ListenerForHotkeys:
    def __init__(self, app):
        self.app = app
        self.turn_on_hotkey = "ctrl_l + f2"
        self.turn_off_hotkey = "ctrl_l + f3"
        self.input = ""
        self.last_press = ""
        #  There is an error while typing ctrl+a for instance (a is not visible)
        #  If the user presses either ctrl_l or ctrl_r this number will increase to 1
        #  Than on_press will unpress this button and on_release will get notified of it and do nothing
        #  to avoid any possible consequences of doing that
        self.fix_against_ctrl_l = 0
        self.fix_against_ctrl_r = 0
        # Our listener
        self.listener = ""

    def start_listening(self):
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def stop_listening(self):
        self.listener.stop()

    def on_press(self, key):
        print("ListenerForHotkeys is working")
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
            if self.input == self.turn_on_hotkey:
                self.app.start_autoclicker()
            if self.input == self.turn_off_hotkey:
                self.app.stop_autoclicker()
            self.last_press = ""
            self.input = ""
            self.fix_against_ctrl_l = 0
            self.fix_against_ctrl_r = 0

    def change_turn_on_hotkey(self, sequence):
        self.turn_on_hotkey = sequence

    def change_turn_off_hotkey(self, sequence):
        self.turn_off_hotkey = sequence
