import tkinter as tk


class GUIChangeHotkeys(tk.Toplevel):
    def __init__(self, listener):
        tk.Toplevel.__init__(self)
        tk.Toplevel.title(self, "")
        tk.Toplevel.protocol(self, "WM_DELETE_WINDOW", self.stop_listening)
        self.resizable(False, False)
        self.listener = listener
        tk.Label(self, text="Press two buttons to make a new hotkey").pack()
        tk.Toplevel.wait_window(self)

    def stop_listening(self):
        self.listener.stop()
        tk.Toplevel.destroy(self)
