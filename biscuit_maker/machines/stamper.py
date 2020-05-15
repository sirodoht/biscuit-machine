from enum import Enum
from biscuit_maker.biscuit import Biscuit, BiscuitStates


class StamperCodes(Enum):
    STAMP = "STAMP"


class StamperMachine():
    def __init__(self):
        pass

    def send_signal(self, state):
        """Base interface for sending signals to the machine."""
        if state[2] == BiscuitStates.DOLLOP:
            state[2] = BiscuitStates.STAMPED

    def read_value(self, code):
        """Get current state of biscuit at the position of Stamper"""
        return state[2]
