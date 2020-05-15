import time
from enum import Enum
from biscuit_maker.machines.machine import Machine, MachineCodes


class MotorCodes(Enum):
    MOTOR_PULSE = "MOTOR_PULSE"


class MotorMachine(Machine):

    def __init__(self):
        super().__init__()
        self._state = MachineCodes.OFF

    def send_signal(self, code, **args):
        """Base interface for sending signals to the machine."""
        if code == MachineCodes.ON:
            self._state = MachineCodes.ON
        elif code == MachineCodes.OFF:
            self._state = MachineCodes.OFF

    def read_value(self, code):
        """"""


def motor_loop(motor, queue):
    counter = 0
    while True:
        if motor._state == MachineCodes.ON:
            counter += 1
        else:
            counter = 0

        if counter > 20:
            queue.put(MotorCodes.MOTOR_PULSE)
            counter = 0
        time.sleep(0.1)