"""
The pymitv.Control module is in charge of sending keystrokes to the TV.
"""
import time
import requests


class Control:
    """A virtual remove control for the TV."""
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

    @staticmethod
    def send_keystrokes(ip, keystrokes):
        """Connects to TV and sends keystroke via HTTP."""
        tv_url = 'http://{}:6095/controller?action=keyevent&keycode='.format(ip)

        for keystroke in keystrokes:
            if keystroke == 'wait':

                time.sleep(0.4)
            else:
                request = requests.get(tv_url + keystroke)

                if request.status_code != 200:
                    return False

        return True

    @staticmethod
    def mute(ip):
        """Polyfill for muting the TV."""
        tv_url = 'http://{}:6095/controller?action=keyevent&keycode='.format(ip)

        count = 0
        while count > 30:
            count = count + 1
            request = requests.get(tv_url + 'volumedown')

            if request.status_code != 200:
                return False

        return True
