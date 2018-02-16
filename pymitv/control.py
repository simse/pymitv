import requests
import time


class Control:
    turn_on = ['power']
    turn_off = ['power']
    sleep = ['power', 'wait', 'right', 'wait', 'right', 'wait', 'enter']
    wake = ['power']
    up = ['up']
    down = ['down']
    right = ['right']
    left = ['left']
    home = ['home']
    enter = ['enter']
    back = ['back']
    menu = ['menu']
    volume_down = ['volumedown']
    volume_up = ['volumeup']

    def __init__(self):
        print()

    def send_keystrokes(self, ip, keystrokes):
        tv_url = 'http://{}:6095/controller?action=keyevent&keycode='.format(ip)

        for keystroke in keystrokes:
            if keystroke == 'wait':

                time.sleep(0.4)
            else:
                r = requests.get(tv_url + keystroke)

                if r.status_code != 200:
                    return False

        return True

    def mute(self, ip):
        tv_url = 'http://{}:6095/controller?action=keyevent&keycode='.format(ip)

        for x in range(0, 30):
            r = requests.get(tv_url + 'volumedown')

            if r.status_code != 200:
                return False

        return True