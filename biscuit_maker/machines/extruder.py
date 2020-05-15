from enum import Enum
from biscuit_maker.biscuit import Biscuit, BiscuitStates
from biscuit_maker.machines.machine import Machine, MachineCodes


class ExtruderCodes(Enum):
    EXTRUDE = "EXTRUDE"


class ExtruderMachine(Machine):

    def __init__(self):
        self._state = MachineCodes.OFF
        pass

    def send_signal(self, state, code):
        """Base interface for sending signals to the machine."""
        if code == MachineCodes.ON:
            self._state = MachineCodes.ON
        elif code == MachineCodes.OFF:
            self._state = MachineCodes.OFF

        if code == ExtruderCodes.EXTRUDE:
            print("EXTURDER: extruding")
            state[0] == state[0].process(BiscuitStates.DOLLOP)

    def read_value(self, code):
        """Get current state of biscuit at the position of Extruder"""
        return state[0]
