import time
from enum import Enum
from biscuit_maker.biscuit import Biscuit, BiscuitStates
from biscuit_maker.machines.machine import Machine, MachineCodes

class OvenCodes(Enum):
    BAKE = "BAKE"

class OvenHeating(Enum):
    ON = "ON"
    OFF = "OFF"

class OvenMachine(Machine):
    def __init__(self):
        self._current_temp = 20
        self._state = MachineCodes.OFF
        self._heating = OvenHeating.OFF

    def send_signal(self, code):
        """Base interface for sending signals to the machine."""
        if code == MachineCodes.ON:
            self._state = MachineCodes.ON
        elif code == MachineCodes.OFF:
            self._state = MachineCodes.OFF

    def read_value(self, belt):
        """Get current states of biscuits in oven's part of the belt"""
        return (belt[4], belt[5])

    def get_temp(self):
        return self._current_temp

    def enable_heating(self):
        self._heating = OvenHeating.ON

    def disable_heating(self):
        self._heating = OvenHeating.OFF

    def pulse(self):
        if self._heating == OvenHeating.ON:
            self._current_temp += 3
        elif self._heating == OvenHeating.OFF:
            self._current_temp -= 3


def oven_loop(oven):
    """fucks with the oven temp"""
    while True:
        oven.pulse()
        time.sleep(0.05)
