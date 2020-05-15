from enum import Enum

from biscuit_maker.machines.oven import OvenMachine
from biscuit_maker.machines.extruder import ExtruderMachine
from biscuit_maker.machines.stamper import StamperMachine

class MachineCodes(Enum):
    ON = "ON"
    OFF = "OFF"
    PAUSE = "PAUSE"


class Machine():
    """Base class for machines"""

    def __init__(self):
        """"""
        self._state = MachineCodes.OFF
        self.oven_machine = OvenMachine()
        self.extruder_machine = ExtruderMachine()
        self.stamper_machine = StamperMachine()

    def send_signal(self, code):
        """Base interface for sending signals to the machine."""
        self._state = code

    def read_value(self):
        """Base interface for reading machine values."""
        return self._state
