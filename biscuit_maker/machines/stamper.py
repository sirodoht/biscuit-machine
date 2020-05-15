from enum import Enum
from biscuit_maker.biscuit import Biscuit, BiscuitStates
from biscuit_maker.machines.machine import Machine, MachineCodes


class StamperCodes(Enum):
    STAMP = "STAMP"


class StamperMachine(Machine):
    def __init__(self):
        self._state = MachineCodes.OFF

    def send_signal(self, state, code):
        """Base interface for sending signals to the machine."""
        if code == StamperCodes.STAMP:
            print("STAMPER: stamping")
            if state[2] == BiscuitStates.DOLLOP:
                state[2] == state[2].process(code)

        if code == MachineCodes.ON:
            self._state = MachineCodes.ON
        elif code == MachineCodes.OFF:
            self._state = MachineCodes.OFF

    def read_value(self, code):
        """Get current state of biscuit at the position of Stamper"""
        return state[2]
