from enum import Enum
from biscuit_maker.biscuit import Biscuit, BiscuitStates


class OvenCodes(Enum):
    INCREASE_TEMP = "INCREASE_TEMP"
    DECREASE_TEMP = "DECREASE_TEMP"


class OvenMachine():
    def __init__(self):
        self._current_temp = 0

    def send_signal(self, belt, **args):
        """Base interface for sending signals to the machine."""
        oven_positions = [4, 5]
        for position in oven_positions:
            if belt[position] == BiscuitStates.STAMPED:
                belt[position] = BiscuitStates.BAKED_SEMI
            elif belt[position] == BiscuitStates.BAKED_SEMI:
                belt[position] = BiscuitStates.BAKED_FULLY
            elif belt[position] == BiscuitStates.BAKED_FULLY:
                belt[position] = BiscuitStates.BAKED_BURNED

    def read_value(self, belt):
        """Get current states of biscuits in oven's part of the belt"""
        return (belt[4], belt[5])
