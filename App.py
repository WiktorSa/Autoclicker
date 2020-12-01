from threading import Thread
import sys
from GUI import GUI
from Autoclicker import Autoclicker
from ListenerForHotkeys import ListenerForHotkeys
from ListenerChangeHotkeys import ListenerChangeHotkeys


class App:
    def __init__(self):
        #  We turn on all the classes responsible for the work of our program
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
        if not self.run_autoclicker.is_alive():
            self.run_autoclicker.start()

    def stop_autoclicker(self):
        if self.run_autoclicker.is_alive():
            self.autoclicker.turn_off()
            self.run_autoclicker = Thread(target=self.autoclicker.turn_on)

    def change_turn_on_hotkey(self):
        self.listener_change_hotkeys.start_listening()
        print("Something should change")
    #    changed_key = self.changing_hotkeys.get_hotkey()
    #    self.listener.change_turn_on_hotkey(changed_key)

    def turn_off(self):
        if self.run_autoclicker.is_alive():
            self.autoclicker.turn_off()
        sys.exit()


if __name__ == "__main__":
    App()
