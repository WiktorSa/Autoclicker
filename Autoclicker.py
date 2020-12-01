import time
import win32api
import win32con


class Autoclicker:
    def __init__(self):
        self.wait_time = 1
        self.working = False

    def turn_on(self):
        self.working = True
        while self.working:
            print("Autoclicker is working")
            time.sleep(self.wait_time)
            #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def turn_off(self):
        print("Autoclicker stopped")
        self.working = False

    def change_wait_time(self, wait_time):
        self.wait_time = wait_time
