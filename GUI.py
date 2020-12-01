import tkinter as tk


class GUI(tk.Tk):
    def __init__(self, app):
        self.app = app
        tk.Tk.__init__(self)
        tk.Tk.title(self, "Autoclicker")
        self.resizable(False, False)
        tk.Tk.geometry(self, "400x200")
        #    for i in range(6):
        #        tk.Tk.columnconfigure(self, i, weight=1)
        #        tk.Tk.rowconfigure(self, i, weight=1)
        tk.Label(self, text="There will be options there").grid(row=0, columnspan=5)
        tk.Label(self, text="How often should it be done").grid(row=1, column=3, columnspan=3)
        tk.Label(self, text="Options to set the time").grid(row=2, column=3, columnspan=3)
        tk.Label(self, text="Start Hotkey").grid(row=3, column=4, columnspan=2)
        tk.Button(self, text="ctrl_l + f2", command=self.app.change_turn_on_hotkey).grid(
            row=4, column=4, columnspan=2)
        tk.Label(self, text="Stop Hotkey").grid(row=3, column=6)
        tk.Button(self, text="ctrl_l + f3", command=None).grid(row=4, column=6, columnspan=2)
        tk.Button(self, text="START", command=self.app.start_autoclicker).grid(row=5, column=5, padx=5)
        tk.Button(self, text="STOP", command=self.app.stop_autoclicker).grid(row=5, column=6, padx=5)
        tk.Button(self, text="EXIT", command=self.app.turn_off).grid(row=5, column=7, padx=5)

    def change_hotkeys_buttons(self, hotkey):
        print("Value changed to " + hotkey)
