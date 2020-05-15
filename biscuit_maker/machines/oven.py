from enum import Enum
from biscuit_maker.machines.machine import Machine, MachineCodes


class OvenCodes(Enum):
    INCREASE_TEMP = "INCREASE_TEMP"
    DECREASE_TEMP = "DECREASE_TEMP"


class OvenMachine(Machine):

    def __init__(self):
        super().__init__(self)
        self._temp = 0

    def send_signal(self, code, **args):
        """Base interface for sending signals to the machine."""

    def read_value(self, code):
        """"""