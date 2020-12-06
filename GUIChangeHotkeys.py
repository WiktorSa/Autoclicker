import tkinter as tk


class GUIChangeHotkeys(tk.Toplevel):
    def __init__(self, listener):
        tk.Toplevel.__init__(self)
        tk.Toplevel.title(self, "")
        tk.Toplevel.protocol(self, "WM_DELETE_WINDOW", self.stop_listening)
        tk.Toplevel.iconbitmap(self, "white.ico")
        self.resizable(False, False)
        self.listener = listener
        self.text = tk.Label(self, text="Press two buttons to make a new hotkey", font=('Helvetica', 12))
        self.text.pack()

    # If the user closes the window the listening will stop immediately
    def stop_listening(self):
        self.listener.stop()
        tk.Toplevel.destroy(self)

    #  If the user fails to press two keys at the same time the text will change to inform the user of the wrong input
    def change_text(self):
        self.text.config(text="Wrong input. Try again. Remember you need to press two buttons to make a new hotkey")
