"""
The pymitv.Control module is in charge of sending keystrokes to the TV.
"""
import time
import json
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
    def send_keystrokes(ip_address, keystrokes, wait=False):
        """Connects to TV and sends keystroke via HTTP."""
        tv_url = 'http://{}:6095/controller?action=keyevent&keycode='.format(ip_address)

        for keystroke in keystrokes:
            if keystroke == 'wait' or wait is True:

                time.sleep(0.7)
            else:
                request = requests.get(tv_url + keystroke)

                if request.status_code != 200:
                    return False

        return True

    @staticmethod
    def change_source(ip_address, source):
        """Select source hdmi1 or hdmi2"""
        tv_url = 'http://{}:6095/controller?action=changesource&source='.format(ip_address)
        source = source
        request = requests.get(tv_url + source)
        if request.status_code != 200:
            return False

        return True

    @staticmethod
    def mute(ip_address):
        """Polyfill for muting the TV."""
        tv_url = 'http://{}:6095/controller?action=keyevent&keycode='.format(ip_address)

        count = 0
        while count > 30:
            count = count + 1
            request = requests.get(tv_url + 'volumedown')

            if request.status_code != 200:
                return False

        return True

    @staticmethod
    def check_state(ip_address):
        """Check if xiaomi tv is reachable"""
        request_timeout = 0.1

        try:
            tv_url = 'http://{}:6095/request?action=isalive'.format(ip_address)
            requests.get(tv_url, timeout=request_timeout)
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError):
            return False

        return True

    @staticmethod
    def get_volume(ip_address):
        """Get the current volume of xiaomi tv"""
        request_timeout = 0.1

        try:
            tv_url = 'http://{}:6095/general?action=getVolum'.format(ip_address)
            request = requests.get(tv_url, timeout=request_timeout)
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError):
            return False

        volume = json.loads(request.json()['data'])['volum']
        return volume
