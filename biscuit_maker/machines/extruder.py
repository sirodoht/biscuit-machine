from enum import Enum
from biscuit_maker.biscuit import Biscuit, BiscuitStates


class ExtruderCodes(Enum):
    EXTRUDE = "EXTRUDE"


class ExtruderMachine():

    def __init__(self):
        pass

    def send_signal(self, state, code):
        """Base interface for sending signals to the machine."""
        if code == ExtruderCodes.EXTRUDE:
            state[0] == state[0].process(BiscuitStates.DOLLOP)

    def read_value(self, code):
        """Get current state of biscuit at the position of Extruder"""
        return state[0]
