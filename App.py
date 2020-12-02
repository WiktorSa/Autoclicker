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
        self.gui = GUI(self)
        self.autoclicker = Autoclicker()
        self.listener_for_hotkeys = ListenerForHotkeys(self)
        self.listener_change_hotkeys = ListenerChangeHotkeys()
        #  Declaring all the variables that will be important
        self.run_autoclicker = Thread(target=self.autoclicker.turn_on)
        #  Turning on all the functionalities of the programss
        self.listener_for_hotkeys.start_listening()
        self.gui.mainloop()

    def start_autoclicker(self):
        #  Only one autoclicker can run at the time
        if not self.run_autoclicker.is_alive():
            self.run_autoclicker.start()

    def stop_autoclicker(self):
        if self.run_autoclicker.is_alive():
            self.autoclicker.turn_off()
            self.run_autoclicker = Thread(target=self.autoclicker.turn_on)

    def change_hotkey(self):
        #  We stop listening for hotkeys that will turn on autoclicker (for safety)
        self.listener_for_hotkeys.stop_listening()
        #  Than we start listening for the change that user wants to do (warning - we cannot just create an
        #  instance of this class every time we want to change hotkey because than we wouldn't be able
        #  to get a hotkey from the function)
        self.listener_change_hotkeys.start_listening()
        print("Something should change")

    def turn_off(self):
        if self.run_autoclicker.is_alive():
            self.autoclicker.turn_off()
        sys.exit()


if __name__ == "__main__":
    App()
