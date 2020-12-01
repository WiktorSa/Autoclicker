import tkinter as tk


class GUIChangeHotkeys(tk.Tk):
    def __init__(self, listener):
        tk.Tk.__init__(self)
        tk.Tk.title(self, "")
        self.listener_to_hotkeys = listener
        self.protocol("WM_DELETE_WINDOW", self.closing)
        self.resizable(False, False)
        tk.Label(self, text="Press two buttons to make a new hotkey").pack()

    def closing(self):
        self.listener_to_hotkeys.stop()
        self.quit()
        self.destroy()
