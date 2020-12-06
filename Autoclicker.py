import time
import win32api
import win32con


class Autoclicker:
    def __init__(self):
        self.minutes_time = 0
        self.seconds_time = 5
        self.one_tenth_seconds_time = 0
        self.one_hundred_seconds_time = 0
        self.which_mouse_click = "Left"
        self.is_working = False

    def turn_on(self):
        how_many_one_hundred_seconds_should_pass_before_press = self.minutes_time * 6000 + self.seconds_time * 100 + \
                                                    self.one_tenth_seconds_time * 10 + self.one_hundred_seconds_time
        self.is_working = True
        while self.is_working:
            if self.which_mouse_click == "Left":
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            else:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
            for i in range(how_many_one_hundred_seconds_should_pass_before_press):
                time.sleep(0.01)
                if not self.is_working:
                    break

    def turn_off(self):
        self.is_working = False

    def get_minutes_time(self):
        return self.minutes_time

    def get_seconds_time(self):
        return self.seconds_time

    def get_one_tenth_seconds_time(self):
        return self.one_tenth_seconds_time

    def get_one_hundred_seconds_time(self):
        return self.one_hundred_seconds_time

    def change_time(self, which_time, how_much):
        if which_time == "minutes":
            self.minutes_time += how_much
        elif which_time == "seconds":
            self.seconds_time += how_much
        elif which_time == "1/10":
            self.one_tenth_seconds_time += how_much
        else:
            self.one_hundred_seconds_time += how_much

    def change_mouse_click(self, option):
        self.which_mouse_click = option
