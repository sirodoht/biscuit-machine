import time
import threading
from queue import Queue
from biscuit_maker.machines.machine import MachineCodes, Machine
from biscuit_maker.machines.motor import MotorCodes, MotorMachine, motor_loop
from biscuit_maker.biscuit import Biscuit

machine = Machine()
state = [
    Biscuit(),
    Biscuit(),
    Biscuit(),
    Biscuit(),
    Biscuit(),
    Biscuit(),
    Biscuit(),
    Biscuit(),
]

def main():
    """
    sets up main threads
    """
    the_queue = Queue()
    motor_queue = Queue()
    the_motor = MotorMachine()

    the_input = threading.Thread(target=input_loop, args=(the_queue,))
    motor_thread = threading.Thread(target=motor_loop, args=(the_motor, motor_queue))
    the_bisquit = threading.Thread(target=main_loop, args=(the_motor, the_queue, motor_queue))

    the_input.start()
    motor_thread.start()
    the_bisquit.start()
    the_queue.join()
    motor_queue.join()


def input_loop(the_queue):
    """Checks for user input and puts it into the queue"""
    while True:
        user_command = input().strip().lower()
        the_queue.put(user_command)


def main_loop(motor, the_queue, motor_queue):
    machine = Machine()
    while True:
        user_command = ""
        try:
            user_command = the_queue.get_nowait()
        except:
            pass

        motor_signal = None
        try:
            motor_signal = motor_queue.get(block=False)
        except:
            pass

        if motor_signal == MotorCodes.MOTOR_PULSE:
            motor_queue.task_done()
            print("got a pulse!")

        if user_command:
            the_queue.task_done()
            if user_command == "on":
                machine.send_signal(MachineCodes.ON)
                motor.send_signal(MachineCodes.ON)
                print("Switch is ON")
            elif user_command == "off":
                machine.send_signal(MachineCodes.OFF)
                print("Switch is OFF")
            elif user_command == "pause":
                machine.send_signal(MachineCodes.PAUSE)
                print("Switch is PAUSED")
        if machine.read_value() == MachineCodes.ON:
            if machine.oven_machine.current_temp < 220:
                machine.oven_machine.send_signal(OvenMachine.HEATING_ON)
            else:
                machine.oven_machine.send_signal(OvenMachine.HEATING_OFF)

            machine.extruder_machine.send_signal(state, ExtruderMachine.EXTRUDE)
            machine.stamper_machine.send_signal(state, StamperMachine.STAMP)
            machine.oven_machine.send_signal(state, OvenMachine.BAKE)
        elif machine.read_value() == MachineCodes.ON:
            machine.oven_machine.send_signal(state, OvenMachine.BAKE)
        time.sleep(0.1)


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)
