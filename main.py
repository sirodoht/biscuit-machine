import time
import threading
from queue import Queue
from biscuit_maker.machines.machine import MachineCodes, Machine
from biscuit_maker.machines.motor import MotorCodes, MotorMachine, motor_loop
from biscuit_maker.machines.oven import OvenCodes, OvenMachine, oven_loop
from biscuit_maker.machines.extruder import ExtruderCodes, ExtruderMachine
from biscuit_maker.machines.stamper import StamperCodes, StamperMachine
from biscuit_maker.biscuit import Biscuit


def main():
    """
    sets up main threads
    """
    the_queue = Queue()
    motor_queue = Queue()

    the_motor = MotorMachine()
    the_oven = OvenMachine()
    the_extruder = ExtruderMachine()
    the_stamper = StamperMachine()

    the_input = threading.Thread(target=input_loop, args=(the_queue,))
    motor_thread = threading.Thread(target=motor_loop, args=(the_motor, motor_queue))
    oven_thread = threading.Thread(target=oven_loop, args=(the_oven,))
    the_bisquit = threading.Thread(target=main_loop, args=(the_motor, the_oven, the_extruder, the_stamper, the_queue, motor_queue))

    the_input.start()
    oven_thread.start(  )
    motor_thread.start()
    the_bisquit.start()
    the_queue.join()
    motor_queue.join()


def input_loop(the_queue):
    """Checks for user input and puts it into the queue"""
    while True:
        user_command = input("Operator input: ").strip().lower()
        the_queue.put(user_command)


def main_loop(motor, oven, extruder, stamper, the_queue, motor_queue):
    just_turned_on = False

    # presumption, our conveyor belt deals with 8 biscuits at a time.
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
    main_state = "off"

    while True:
        user_command = ""
        try:
            user_command = the_queue.get_nowait()
        except:
            pass

        motor_pulse = None
        try:
            motor_pulse = motor_queue.get(block=False)
        except:
            pass

        if motor_pulse == MotorCodes.MOTOR_PULSE:
            motor_queue.task_done()
            print("got a pulse!")

        if user_command:
            the_queue.task_done()
            if user_command == "on":
                motor.send_signal(MachineCodes.ON)
                oven.send_signal(MachineCodes.ON)
                # oven.enable_heating()
                extruder.send_signal(state, MachineCodes.OFF)
                stamper.send_signal(state, MachineCodes.OFF)
                just_turned_on = True
                main_state = user_command
                print("Switch is ON")
            elif user_command == "off":
                motor.send_signal(MachineCodes.OFF)
                oven.send_signal(MachineCodes.OFF)
                oven.disable_heating()
                extruder.send_signal(state, MachineCodes.OFF)
                stamper.send_signal(state, MachineCodes.OFF)
                just_turned_on = False
                main_state = user_command
                print("Switch is OFF")
            elif user_command == "pause":
                # paused, stop the motor.
                motor.send_signal(MachineCodes.OFF)
                extruder.send_signal(state, MachineCodes.OFF)
                stamper.send_signal(state, MachineCodes.OFF)
                main_state = user_command
                print("Switch is PAUSED")


        if main_state == "off":
            continue

        oven_temp = oven.get_temp()
        # 1. read oven temp. If we just turned on we need to skip/continue until we are hot
        if just_turned_on and abs(oven_temp) > 220:
            just_turned_on = False
            time.sleep(0.1)
            continue

        # 2. regulate oven to be between 220 - 240
        if oven_temp < 220:
            print("Oven temp too cold, regulating", oven_temp)
            oven.enable_heating()
            time.sleep(0.1)
            continue
        elif oven_temp > 240:
            oven.disable_heating()
            print("Oven temp too hot, regulating", oven_temp)
            time.sleep(0.1)
            continue

        # 3. cookie extruder
        # we have reached this step which means oven is good
        if motor_pulse:
            # tell extruder to extrude and change the state of our internal representation.
            extruder.send_signal(state, ExtruderCodes.EXTRUDE)
            # tell the stamper to perform and change internal state.
            stamper.send_signal(state, StamperCodes.STAMP)

        #     # oven is baking biscuits at positions 4 and 5
        #     oven_positions = [4, 5]
        #     for position in oven_positions:
        #         if belt[position] == BiscuitStates.STAMPED:
        #             belt[position] = belt[position].process(BiscuitStates.BAKED_SEMI)
        #         elif belt[position] == BiscuitStates.BAKED_SEMI:
        #             belt[position] = belt[position].process(BiscuitStates.BAKED_FULLY)
        #         elif belt[position] == BiscuitStates.BAKED_FULLY:
        #             belt[position] = belt[position].process(BiscuitStates.BAKED_BURNED)


        time.sleep(0.1)


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)
