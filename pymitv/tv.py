"""Contains the class for interfacing with the TV."""
from pymitv import Control
from pymitv import Navigator


class TV:
    """A virtual representation of the TV that stores state, and takes controls."""
    ip = None
    state = True
    source = None

    def __init__(self, ip=None, initialized=False):
        # Check if an IP address has been supplied to the constructor
        if ip is None:
            print('No TV supplied, hence it won\'t work')

        # Check if TV has been initialized for pymitv control
        if initialized is False:
            print('If the TV hasn\'t been setup for full pymitv control, \
using any of the polyfill controls, could produce weird results.')

        # Make IP address global regardless of value
        self.ip = ip

    def _send_keystroke(self, keystroke, wait=False):
        # Check if an IP address has been supplied, if it hasn't return false.
        if self.ip is None:
            return False

        # Make sure the TV is not already on, and then send keystroke
        return Control().send_keystrokes(self.ip, keystroke, wait)

        # Send True regardless of whether or not command was sent
        #return True

    @property
    def is_on(self):
        """Returns the assumed state of the TV."""
        return self.state

    def wake(self):
        """Wakes up the TV from sleep."""
        return self._send_keystroke(Control.wake)

    def sleep(self):
        """Puts the TV to sleep."""
        return self._send_keystroke(Control.sleep)

    def turn_off(self):
        """Turns off the TV completely."""
        return self._send_keystroke(Control.turn_off)

    def enter(self):
        """Presses enter to affirm."""
        return self._send_keystroke(Control.enter)

    def menu(self):
        """Opens the menu."""
        return self._send_keystroke(Control.menu)

    def home(self):
        """Goes home."""
        return self._send_keystroke(Control.home)

    def back(self):
        """Goes back."""
        return self._send_keystroke(Control.back)

    def up(self):
        """Presses up key."""
        return self._send_keystroke(Control.up)

    def down(self):
        """Presses down key."""
        return self._send_keystroke(Control.down)

    def left(self):
        """Presses left key."""
        return self._send_keystroke(Control.left)

    def right(self):
        """Presses right key."""
        return self._send_keystroke(Control.right)

    def volume_up(self):
        """Turns up the volume by one."""
        return self._send_keystroke(Control.volume_up)

    def volume_down(self):
        """Turns down the volume by one."""
        return self._send_keystroke(Control.volume_down)

    def mute(self):
        """Mutes the TV."""
        return Control().mute(self.ip)

    #def set_source(self, source):
    #    """Selects and saves source."""
    #    self.source = source
    #    route = Navigator(source=self.source).navigate_to_source(source)
    #    print(route)
#
    #    return self._send_keystroke(route, wait=True)