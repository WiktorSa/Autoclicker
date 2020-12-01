import tkinter as tk


class GUIChangeHotkeys(tk.Frame):
    def __init__(self, tk_instance, listener):
        tk.Tk.__init__(tk_instance)
        tk.Tk.title(tk_instance, "")
        self.listener_to_hotkeys = listener
        self.protocol("WM_DELETE_WINDOW", self.closing)
        self.resizable(False, False)
        tk.Label(self, text="Press two buttons to make a new hotkey").pack()

    def closing(self):
        self.listener_to_hotkeys.stop()
        self.quit()
        self.destroy()
