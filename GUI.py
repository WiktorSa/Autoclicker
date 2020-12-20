import tkinter as tk
import pathlib
from tkinter import ttk
from GUIInfo import GUIInfo


class GUI(tk.Tk):
    def __init__(self, app):
        self.app = app
        tk.Tk.__init__(self)
        self.title("Free Autoclicker")
        self.config(bg='white')
        self.iconphoto(True, tk.PhotoImage(file=(str(pathlib.Path(__file__).parent.absolute()) + "\\click.png")))
        self.protocol("WM_DELETE_WINDOW", self.app.turn_off)
        self.resizable(False, False)

        #  Creating styles for our app
        self.styles = ttk.Style()
        self.styles.configure("every.TSeparator", background='D9D9D9')
        self.styles.configure("mainname.TLabel", foreground='blue', background='white', font=('Helvetica', 10, 'bold'))
        self.styles.configure("name.TLabel", background='white', font=('Helvetica', 9))
        self.styles.configure("display.TLabel", background='white', borderwidth=2, relief='solid', font=3)
        self.styles.configure("choice.TRadiobutton", background='white')
        self.styles.configure("hotkey.TLabel", background='white')

        #  Design of the info and manual
        self.info_button = HoveringButton(self, text="Info", command=self.create_info_gui)
        self.info_button.grid(row=0, column=0, sticky='w')

        self.vertical_line_up = ttk.Separator(self, orient=tk.VERTICAL, style="every.TSeparator")
        self.vertical_line_up.grid(row=1, column=0, columnspan=9, sticky='ew')
        self.vertical_line_down = ttk.Separator(self, orient=tk.VERTICAL, style="every.TSeparator")
        self.vertical_line_down.grid(row=9, column=0, columnspan=9, sticky='ew', pady=(5, 7))

        # Design of click interval
        self.click_interval_vertical_line_up = ttk.Separator(self, orient=tk.VERTICAL, style="every.TSeparator")
        self.click_interval_vertical_line_up.grid(row=2, column=0, columnspan=9, sticky='ew')

        self.click_interval_name = ttk.Label(self, text="Click Interval", style="mainname.TLabel")
        self.click_interval_name.grid(row=2, column=1, columnspan=2)

        self.click_interval_minutes_name = ttk.Label(self, text="Minutes", style="name.TLabel")
        self.click_interval_minutes_name.grid(row=3, column=1, columnspan=2)
        self.click_interval_minutes_display = ttk.Label(self, text=" " + str(self.app.get_time("minutes")),
                                                        style='display.TLabel')
        self.click_interval_minutes_display.grid(row=4, column=1, rowspan=2, sticky='e')
        self.click_interval_minutes_up = tk.Button(self, text="▲", command=lambda: self.app.increase_time("minutes"))
        self.click_interval_minutes_up.grid(row=4, column=2, sticky='w')
        self.click_interval_minutes_down = tk.Button(self, text="▼", command=lambda: self.app.decrease_time("minutes"))
        self.click_interval_minutes_down.grid(row=5, column=2, sticky='w', pady=(0, 5))

        self.click_interval_seconds_name = ttk.Label(self, text="Seconds", style="name.TLabel")
        self.click_interval_seconds_name.grid(row=3, column=3, columnspan=2)
        self.click_interval_seconds_display = ttk.Label(self, text=" " + str(self.app.get_time("seconds")),
                                                        style='display.TLabel')
        self.click_interval_seconds_display.grid(row=4, column=3, rowspan=2, sticky='e')
        self.click_interval_seconds_up = tk.Button(self, text="▲", command=lambda: self.app.increase_time("seconds"))
        self.click_interval_seconds_up.grid(row=4, column=4, sticky='w')
        self.click_interval_seconds_down = tk.Button(self, text="▼", command=lambda: self.app.decrease_time("seconds"))
        self.click_interval_seconds_down.grid(row=5, column=4, sticky='w', pady=(0, 5))

        self.click_interval_tenth_second_name = ttk.Label(self, text="1/10 Second", style="name.TLabel")
        self.click_interval_tenth_second_name.grid(row=3, column=5, columnspan=2)
        self.click_interval_tenth_second_display = ttk.Label(self, text=" " + str(self.app.get_time("1/10")),
                                                             style='display.TLabel')
        self.click_interval_tenth_second_display.grid(row=4, column=5, rowspan=2, sticky='e')
        self.click_interval_tenth_second_up = tk.Button(self, text="▲", command=lambda: self.app.increase_time("1/10"))
        self.click_interval_tenth_second_up.grid(row=4, column=6, sticky='w')
        self.click_interval_tenth_second_down = tk.Button(self, text="▼",
                                                          command=lambda: self.app.decrease_time("1/10"))
        self.click_interval_tenth_second_down.grid(row=5, column=6, sticky='w', pady=(0, 5))

        self.click_interval_hundred_second_name = ttk.Label(self, text="1/100 Second", style="name.TLabel")
        self.click_interval_hundred_second_name.grid(row=3, column=7, columnspan=2)
        self.click_interval_hundred_second_display = ttk.Label(self, text=" " + str(self.app.get_time("1/100")),
                                                               style='display.TLabel')
        self.click_interval_hundred_second_display.grid(row=4, column=7, rowspan=2, sticky='e')
        self.click_interval_hundred_second_up = tk.Button(self, text="▲",
                                                          command=lambda: self.app.increase_time("1/100"))
        self.click_interval_hundred_second_up.grid(row=4, column=8, sticky='w')
        self.click_interval_hundred_second_down = tk.Button(self, text="▼",
                                                            command=lambda: self.app.decrease_time("1/100"))
        self.click_interval_hundred_second_down.grid(row=5, column=8, sticky='w', pady=(0, 5))

        # Design of click option
        self.click_option_vertical_line_up = ttk.Separator(self, orient=tk.VERTICAL, style="every.TSeparator")
        self.click_option_vertical_line_up.grid(row=6, column=0, columnspan=9, sticky='ew')

        self.click_option_name = ttk.Label(self, text="Click Options", style="mainname.TLabel")
        self.click_option_name.grid(row=6, column=1, columnspan=2)
        option = tk.StringVar()
        option.set("Left")

        self.click_option_option_1 = ttk.Radiobutton(self, text="Left Click", style="choice.TRadiobutton",
                                                     variable=option, value="Left",
                                                     command=lambda: self.app.change_mouse_click(option))
        self.click_option_option_1.grid(row=7, column=1, columnspan=2, sticky='w')

        self.click_option_option_2 = ttk.Radiobutton(self, text="Right Click", style="choice.TRadiobutton",
                                                     variable=option, value="Right",
                                                     command=lambda: self.app.change_mouse_click(option))
        self.click_option_option_2.grid(row=8, column=1, columnspan=2, sticky='w')

        self.horizontal_line_seperator_right = ttk.Separator(self, orient=tk.HORIZONTAL, style="every.TSeparator")
        self.horizontal_line_seperator_right.grid(row=6, column=4, rowspan=4, sticky="nse")

        #  Desing of Click Hotkey
        self.click_hotkey_name = ttk.Label(self, text="Click Hotkey", style="mainname.TLabel")
        self.click_hotkey_name.grid(row=6, column=5, columnspan=2)

        self.click_hotkey_turn_on_label = ttk.Label(self, text="Start Hotkey", style="hotkey.TLabel")
        self.click_hotkey_turn_on_label.grid(row=7, column=5, columnspan=2)
        self.click_hotkey_turn_on = tk.Button(self, text="ctrl_l + f2", command=lambda: self.app.change_hotkey(True))
        self.click_hotkey_turn_on.grid(row=8, column=5, columnspan=2)

        self.click_hotkey_turn_off_label = ttk.Label(self, text="Stop Hotkey", style="hotkey.TLabel")
        self.click_hotkey_turn_off_label.grid(row=7, column=7, columnspan=2)
        self.click_hotkey_turn_off = tk.Button(self, text="ctrl_l + f3", command=lambda: self.app.change_hotkey(False))
        self.click_hotkey_turn_off.grid(row=8, column=7, columnspan=2)

        #  Design of the bottom side of the page
        self.bottom_start = tk.Button(self, text="START", command=self.app.start_autoclicker)
        self.bottom_start.grid(row=10, column=2, columnspan=3, sticky='nwse', padx=5, pady=(0, 5))

        self.bottom_stop = tk.Button(self, text="STOP", bg='#BCBCBC', activebackground='#BCBCBC',
                                     command=self.do_nothing)
        self.bottom_stop.grid(row=10, column=5, columnspan=2, sticky='nwse', padx=5, pady=(0, 5))

        self.bottom_exit = tk.Button(self, text="EXIT", command=self.app.turn_off)
        self.bottom_exit.grid(row=10, column=7, columnspan=2, sticky='nwse', padx=5, pady=(0, 5))

    #  Change the display of hotkeys
    def change_hotkeys(self, hotkey, is_it_turn_on_hotkey):
        if is_it_turn_on_hotkey:
            self.click_hotkey_turn_on.config(text=hotkey)
        else:
            self.click_hotkey_turn_off.config(text=hotkey)

    #  Change the display of time
    def change_time(self, which_time):
        if which_time == "minutes":
            if self.app.get_time(which_time) < 10:
                self.click_interval_minutes_display.config(text=" " + str(self.app.get_time(which_time)))
            else:
                self.click_interval_minutes_display.config(text=str(self.app.get_time(which_time)))

        elif which_time == "seconds":
            if self.app.get_time(which_time) < 10:
                self.click_interval_seconds_display.config(text=" " + str(self.app.get_time(which_time)))
            else:
                self.click_interval_seconds_display.config(text=str(self.app.get_time(which_time)))

        elif which_time == "1/10":
            if self.app.get_time(which_time) < 10:
                self.click_interval_tenth_second_display.config(text=" " + str(self.app.get_time(which_time)))
            else:
                self.click_interval_tenth_second_display.config(text=str(self.app.get_time(which_time)))

        else:
            if self.app.get_time(which_time) < 10:
                self.click_interval_hundred_second_display.config(text=" " + str(self.app.get_time(which_time)))
            else:
                self.click_interval_hundred_second_display.config(text=str(self.app.get_time(which_time)))

    #  command will be used to verify which options should be changed and which should not be changed
    def disable_all_options(self, command):
        self.info_button.config(command=self.do_nothing)
        self.click_interval_minutes_up.config(command=self.do_nothing)
        self.click_interval_minutes_down.config(command=self.do_nothing)
        self.click_interval_seconds_up.config(command=self.do_nothing)
        self.click_interval_seconds_down.config(command=self.do_nothing)
        self.click_interval_tenth_second_up.config(command=self.do_nothing)
        self.click_interval_tenth_second_down.config(command=self.do_nothing)
        self.click_interval_hundred_second_up.config(command=self.do_nothing)
        self.click_interval_hundred_second_down.config(command=self.do_nothing)
        self.click_option_option_1.config(state='disable')
        self.click_option_option_2.config(state='disable')
        self.click_hotkey_turn_on.config(command=self.do_nothing)
        self.click_hotkey_turn_off.config(command=self.do_nothing)
        self.bottom_start.config(command=self.do_nothing)
        if command == "StartAutoclicker":
            self.bottom_start.config(bg='#BCBCBC', activebackground='#BCBCBC')
            self.bottom_stop.config(bg='white', activebackground='white', command=self.app.stop_autoclicker)

    def enable_all_options(self, command):
        self.info_button.config(command=self.create_info_gui)
        self.click_interval_minutes_up.config(command=lambda: self.app.increase_time("minutes"))
        self.click_interval_minutes_down.config(command=lambda: self.app.decrease_time("minutes"))
        self.click_interval_seconds_up.config(command=lambda: self.app.increase_time("seconds"))
        self.click_interval_seconds_down.config(command=lambda: self.app.decrease_time("seconds"))
        self.click_interval_tenth_second_up.config(command=lambda: self.app.increase_time("1/10"))
        self.click_interval_tenth_second_down.config(command=lambda: self.app.decrease_time("1/10"))
        self.click_interval_hundred_second_up.config(command=lambda: self.app.increase_time("1/100"))
        self.click_interval_hundred_second_down.config(command=lambda: self.app.decrease_time("1/100"))
        self.click_option_option_1.config(state='enable')
        self.click_option_option_2.config(state='enable')
        self.click_hotkey_turn_on.config(command=lambda: self.app.change_hotkey(True))
        self.click_hotkey_turn_off.config(command=lambda: self.app.change_hotkey(False))
        self.bottom_start.config(command=self.app.start_autoclicker)
        if command == "StopAutoclicker":
            self.bottom_start.config(bg='white', activebackground='white')
            self.bottom_stop.config(bg='#BCBCBC', activebackground='#BCBCBC', command=self.do_nothing)

    #  I know this function may sound useless but there is no other way to change the button command to None
    #  At least I tried everything and this seems like the only solution
    # noinspection PyMethodMayBeStatic
    def do_nothing(self):
        pass

    def create_info_gui(self):
        self.disable_all_options("InfoGUI")
        info_gui = GUIInfo()
        info_gui.wait_window()
        self.enable_all_options("InfoGUI")


#  This buttons will appear on the top of the app. They will also change background when hovered
class HoveringButton(tk.Button):
    def __init__(self, master, text, command):
        tk.Button.__init__(self, master=master, text=text, command=command, border=0, bg='white',
                           activebackground='light blue')
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    # noinspection PyUnusedLocal
    def on_enter(self, e):
        self.config(bg='light cyan')

    # noinspection PyUnusedLocal
    def on_leave(self, e):
        self.config(bg='white')
