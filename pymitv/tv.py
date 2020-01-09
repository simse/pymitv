"""Contains the class for interfacing with the TV."""
from pymitv import Control
from pymitv import Navigator


class TV:
    """A virtual representation of the TV that stores state, and takes controls."""
    ip_address = None
    state = True
    source = None

    def __init__(self, ip_address=None, source=None, initialized=True, assume_state=True):
        # Check if an IP address has been supplied to the constructor
        if ip_address is None:
            print('No TV supplied, hence it won\'t work')

        # Check if TV has been initialized for pymitv control
        if initialized is False:
            print('If the TV hasn\'t been setup for full pymitv control, \
using any of the polyfill controls, could produce weird results.')

        # Make IP address global regardless of value
        self.ip_address = ip_address

        # Make active source global
        self.source = source

        # Set assume_state
        self.assume_state = assume_state

        # Set volume
        self.volume = Control().get_volume(self.ip_address)

    def _send_keystroke(self, keystroke, wait=False):
        # Check if an IP address has been supplied, if it hasn't return false.
        if self.ip_address is None:
            return False

        # Make sure the TV is not already on, and then send keystroke
        return Control().send_keystrokes(self.ip_address, keystroke, wait)

        # Send True regardless of whether or not command was sent
        #return True

    def change_source(self, source):
        """Change source of xiaomi tv"""
        # Check if an IP address has been supplied, if it hasn't return false.
        if self.ip_address is None:
            return False

        self.source = source
        return Control().change_source(self.ip_address, source)

    def get_volume(self):
        """Get volume of xiaomi tv"""
        # Check if an IP address has been supplied, if it hasn't return false.
        if self.ip_address is None:
            return False

        self.volume = Control().get_volume(self.ip_address)

        return self.volume

    @property
    def is_on(self):
        """Returns the assume state of the TV."""
        if self.assume_state:
            return self.state
        return Control().check_state(self.ip_address)

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
        return Control().mute(self.ip_address)

    def set_source(self, source):
        """Selects and saves source."""
        route = Navigator(source=self.source).navigate_to_source(source)

        # Save new source
        self.source = source

        return self._send_keystroke(route, wait=True)
