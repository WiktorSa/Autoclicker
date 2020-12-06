import tkinter as tk


class GUIInfo(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        tk.Toplevel.title(self, "Info")
        tk.Toplevel.iconbitmap(self, "click.ico")
        self.resizable(False, False)
        self.text = tk.Label(self, text="Free autoclicker made by Wiktor Sadowy\n", font=('Helvetica', 12))
        self.text.pack()
        self.instruction = tk.Label(self, text="How to use it\n", font=('Helvetica', 10, 'bold'))
        self.instruction.pack()
        self.intruction_click_interval_name = tk.Label(self, text="Click Interval", font=('Helvetica', 10, 'bold'))
        self.intruction_click_interval_name.pack()
        self.instruction_click_interval = tk.Label(self, text="Press the arrow up to increase the time between\n"
                                                              " the presses and the arrow down to decrease the time\n")
        self.instruction_click_interval.pack()
        self.intruction_click_options_name = tk.Label(self, text="Click Options", font=('Helvetica', 10, 'bold'))
        self.intruction_click_options_name.pack()
        self.instruction_click_options = tk.Label(self, text="Press the right button to decide which mouse click "
                                                             "to do\n")
        self.instruction_click_options.pack()
        self.intruction_click_hotkey_name = tk.Label(self, text="Click Hotkey", font=('Helvetica', 10, 'bold'))
        self.intruction_click_hotkey_name.pack()
        self.intruction_click_hotkey = tk.Label(self, text="Press the hotkey to change it\n")
        self.intruction_click_hotkey.pack()
        self.intruction_rest_name = tk.Label(self, text="Rest of the options", font=('Helvetica', 10, 'bold'))
        self.intruction_rest_name.pack()
        self.intruction_rest = tk.Label(self, text="Press START to start the program and STOP to stop the program\n"
                                                   "(this can also be done with a proper hotkey)\n"
                                                   "Press EXIT to stop the autoclicker and end the program")
        self.intruction_rest.pack(padx=10, pady=(0, 10))
