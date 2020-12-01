from pynput import keyboard
from GUIChangeHotkeys import GUIChangeHotkeys


class ListenerChangeHotkeys:
    def __init__(self):
        self.hotkey = ""
        self.last_press = ""
        #  The hotkey can only consist of two pressed buttons
        self.length_of_hotkey = 0
        #  There is an error while typing ctrl+a for instance (a is not visible)
        #  If the user presses either ctrl_l or ctrl_r this number will increase to 1
        #  Than on_press will unpress this button and on_release will get notified of it and do nothing
        #  to avoid any possible consequences of doing that
        self.fix_against_ctrl_l = 0
        self.fix_against_ctrl_r = 0
        #  The GUI that will be visible when user prompts to change a hotkey
        self.gui = ""

    def start_listening(self, tk_instance):
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()
        self.gui = GUIChangeHotkeys(tk_instance, listener)
        self.gui.mainloop()

    def on_press(self, key):
        print("ListenerChangeHotkeys is workking")
        try:
            format_key = key.char
        except AttributeError:
            format_key = format(key)
            format_key = format_key[4:]
        if format_key != self.last_press:
            self.length_of_hotkey += 1
            self.last_press = format_key
            if self.hotkey != "":
                self.hotkey = self.hotkey + " + "
            self.hotkey = self.hotkey + str(format_key)
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
            if self.length_of_hotkey == 2:
                #  We first quit the mainloop process and later destory the whole window
                self.gui.quit()
                self.gui.destroy()
                return False
            else:
                self.last_press = ""
                self.hotkey = ""
                self.fix_against_ctrl_l = 0
                self.fix_against_ctrl_r = 0
                self.length_of_hotkey = 0

    def get_hotkey(self):
        return self.hotkey
