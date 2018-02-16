from pymitv import Control

class TV:

    ip = None
    state = False;

    def __init__(self, ip = None):
        #Check if an IP address has been supplied to the constructor
        if(ip == None):
            print('No TV supplied, hence it won\'t work')

        #Make IP address global regardless of value
        self.ip = ip

    def _send_keystroke(self, keystroke):
        #Check if an IP address has been supplied, if it hasn't return false.
        if(self.ip == None):
            return False

        #Make sure the TV is not already on, and then send keystroke
        if(not self.state):
            return Control().send_keystrokes(self.ip, keystroke)

        #Send True regardless of whether or not command was sent, because final goal was still achieved.
        return True

    @property
    def is_on(self):
        # True means on and False means off.
        return self.state

    def wake(self):
        # Uses the local _sendKeystroke function to avoid repetition. DRY code. Ironically, this comment is repeated.
        return self._send_keystroke(Control.wake)

    def sleep(self):
        # Uses the local _sendKeystroke function to avoid repetition. DRY code. Ironically, this comment is repeated.
        return self._send_keystroke(Control.sleep)

    def turn_off(self):
        # Uses the local _sendKeystroke function to avoid repetition. DRY code. Ironically, this comment is repeated.
        return self._send_keystroke(Control.turn_off)

    def enter(self):
        # Uses the local _sendKeystroke function to avoid repetition. DRY code. Ironically, this comment is repeated.
        return self._send_keystroke(Control.enter)

    def menu(self):
        # Uses the local _sendKeystroke function to avoid repetition. DRY code. Ironically, this comment is repeated.
        return self._send_keystroke(Control.menu)

    def home(self):
        # Uses the local _sendKeystroke function to avoid repetition. DRY code. Ironically, this comment is repeated.
        return self._send_keystroke(Control.home)

    def back(self):
        # Uses the local _sendKeystroke function to avoid repetition. DRY code. Ironically, this comment is repeated.
        return self._send_keystroke(Control.back)

    def up(self):
        # Uses the local _sendKeystroke function to avoid repetition. DRY code. Ironically, this comment is repeated.
        return self._send_keystroke(Control.up)

    def down(self):
        # Uses the local _sendKeystroke function to avoid repetition. DRY code. Ironically, this comment is repeated.
        return self._send_keystroke(Control.down)

    def left(self):
        # Uses the local _sendKeystroke function to avoid repetition. DRY code. Ironically, this comment is repeated.
        return self._send_keystroke(Control.left)

    def right(self):
        # Uses the local _sendKeystroke function to avoid repetition. DRY code. Ironically, this comment is repeated.
        return self._send_keystroke(Control.right)

    def volume_up(self):
        # Uses the local _sendKeystroke function to avoid repetition. DRY code. Ironically, this comment is repeated.
        return self._send_keystroke(Control.volume_up)

    def volume_down(self):
        # Uses the local _sendKeystroke function to avoid repetition. DRY code. Ironically, this comment is repeated.
        return self._send_keystroke(Control.volume_down)

    def mute(self):
        # Uses the local _sendKeystroke function to avoid repetition. DRY code. Ironically, this comment is repeated.
        return Control().mute(self.ip)
