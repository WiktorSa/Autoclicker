from threading import Thread
import sys
from GUI import GUI
from GUIChangeHotkeys import GUIChangeHotkeys
from Autoclicker import Autoclicker
from ListenerForHotkeys import ListenerForHotkeys
from ListenerChangeHotkeys import ListenerChangeHotkeys


class App:
    def __init__(self):
        #  We turn on all the main classes responsible for the work of our program
        self.autoclicker = Autoclicker()
        self.listener_for_hotkeys = ListenerForHotkeys(self)
        self.gui = GUI(self)
        #  Declaring all the variables that will be important
        self.run_autoclicker = Thread(target=self.autoclicker.turn_on)
        #  Turning on all the functionalities of the programss
        self.listener_for_hotkeys.start_listening()
        self.gui.mainloop()

    def start_autoclicker(self):
        #  Normally we won't be able to turn on the autoclicker twice but I will still leave it for safety
        if not self.run_autoclicker.is_alive():
            self.gui.disable_all_options("StartAutoclicker")
            self.listener_for_hotkeys.change_listen_for_turn_on_hotkey(False)
            self.run_autoclicker.start()

    def stop_autoclicker(self):
        # As mentioned before. This condition should always be true but if the error occurs it may not be
        if self.run_autoclicker.is_alive():
            self.autoclicker.turn_off()
            self.run_autoclicker = Thread(target=self.autoclicker.turn_on)
            self.listener_for_hotkeys.change_listen_for_turn_on_hotkey(True)
            self.gui.enable_all_options("StopAutoclicker")

    def change_hotkey(self, is_it_turn_on_hotkey):
        self.gui.disable_all_options("ChangeHotkeys")
        self.listener_for_hotkeys.stop_listening()
        listener_change_hotkeys = ListenerChangeHotkeys()
        listener_change_hotkeys.start_listening()
        length_of_hotkey, hotkey = listener_change_hotkeys.get_hotkey()
        if length_of_hotkey == 2:
            self.gui.change_hotkeys(hotkey, is_it_turn_on_hotkey)
            self.listener_for_hotkeys.change_hotkeys(hotkey, is_it_turn_on_hotkey)
        self.listener_for_hotkeys.start_listening()
        self.gui.enable_all_options("ChangeHotkeys")

    def get_time(self, which_time):
        if which_time == "minutes":
            return self.autoclicker.get_minutes_time()
        elif which_time == "seconds":
            return self.autoclicker.get_seconds_time()
        elif which_time == "1/10":
            return self.autoclicker.get_one_tenth_seconds_time()
        else:
            return self.autoclicker.get_one_hundred_seconds_time()

    def increase_time(self, which_time):
        if which_time == "minutes":
            if self.autoclicker.get_minutes_time() + 1 < 60:
                self.autoclicker.change_time(which_time, 1)
                self.gui.change_time(which_time)
        elif which_time == "seconds":
            if self.autoclicker.get_seconds_time() + 1 < 60:
                self.autoclicker.change_time(which_time, 1)
                self.gui.change_time(which_time)
        elif which_time == "1/10":
            if self.autoclicker.get_one_tenth_seconds_time() + 1 < 10:
                self.autoclicker.change_time(which_time, 1)
                self.gui.change_time(which_time)
        else:
            if self.autoclicker.get_one_hundred_seconds_time() + 1 < 10:
                self.autoclicker.change_time(which_time, 1)
                self.gui.change_time(which_time)

    def decrease_time(self, which_time):
        if which_time == "minutes":
            if self.autoclicker.get_minutes_time() - 1 >= 0:
                self.autoclicker.change_time(which_time, -1)
                self.gui.change_time(which_time)
        elif which_time == "seconds":
            if self.autoclicker.get_seconds_time() - 1 >= 0:
                self.autoclicker.change_time(which_time, -1)
                self.gui.change_time(which_time)
        elif which_time == "1/10":
            if self.autoclicker.get_one_tenth_seconds_time() - 1 >= 0:
                self.autoclicker.change_time(which_time, -1)
                self.gui.change_time(which_time)
        else:
            if self.autoclicker.get_one_hundred_seconds_time() - 1 >= 0:
                self.autoclicker.change_time(which_time, -1)
                self.gui.change_time(which_time)

    def change_mouse_click(self, option):
        self.autoclicker.change_mouse_click(option.get())

    def turn_off(self):
        if self.run_autoclicker.is_alive():
            self.autoclicker.turn_off()
        sys.exit()
