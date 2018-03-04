"""
The pymitv.Discover module is in charge of calculating navigation routes on the TV.
"""


class Navigator():

    # Keystroke sequence to open sources menu
    OPEN_SOURCES_IF_NONE = [
        'enter'
    ]

    OPEN_SOURCES_IF_SOURCE_ACTIVE = [
        'home',
        'enter'
    ]

    SOURCE_PATH = {
        'hdmi1': ['enter'],
        'hdmi2': ['right', 'enter'],
        'hdmi3': ['right', 'right', 'enter'],
        'gallery': ['right', 'right', 'right', 'enter'],
        'aux': ['right', 'right', 'right', 'right', 'enter'],
        'tv': ['down', 'enter'],
        'vga': ['down', 'right', 'enter'],
        'av': ['down', 'right', 'right', 'enter'],
        'dtmb': ['down', 'right', 'right', 'right', 'enter'],
    }

    def __init__(self, source=None):
        self.source = source

    def navigate_to_source(self, source):
        keystrokes = []

        if self.source is None:
            keystrokes = keystrokes + self.OPEN_SOURCES_IF_NONE
        else:
            keystrokes = keystrokes + self.OPEN_SOURCES_IF_SOURCE_ACTIVE

        keystrokes = keystrokes + self.SOURCE_PATH[source]

        return keystrokes
