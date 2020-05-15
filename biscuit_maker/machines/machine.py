from enum import Enum

class MachineCodes(Enum):
    MACHINE_OFF = "MACHINE_OFF"
    MACHINE_ON = "MACHINE_ON"
    ON = "ON"
    OFF = "OFF"
    PAUSE = "PAUSE"


class Machine(object):
    """Base class for machines"""

    def __init__(self):
        """"""
        self._state = MachineCodes.MACHINE_OFF

    def send_signal(self, code, **args):
        """Base interface for sending signals to the machine."""

    def read_value(self, code):
        """Base interface for reading machine values."""
