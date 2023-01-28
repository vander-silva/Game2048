#
# from engine_2048 import inputs
#
class UserNavigation:
    def __init__(self):
        self.keyPress = {'left': False, 'right': False, 'up': False, 'down': False, 'noKey': True}

    def get_keypress(self):
        return {dictKey: dictItem for dictItem, dictKey in keyPress.items()}[True]

    def set_keypress(self, key_press):
        for item in self.keyPress:
            self.keyPress[item] = False
        self.keyPress[key_press] = True


def capture_key():
    import win32api as wapi
    import time

    while True:
        left_pressed = wapi.GetAsyncKeyState(37)
        up_pressed = wapi.GetAsyncKeyState(38)
        right_pressed = wapi.GetAsyncKeyState(39)
        down_pressed = wapi.GetAsyncKeyState(40)
        esc_pressed = wapi.GetAsyncKeyState(27)
        if left_pressed:
            return 'left'
            break
        if up_pressed:
            return 'up'
            break
        if right_pressed:
            return 'right'
            break
        if down_pressed:
            return 'down'
            break
        if esc_pressed:
            return 'esc'
            break
        else:
            time.sleep(0.1)
