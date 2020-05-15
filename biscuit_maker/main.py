import time
import threading
from queue import Queue
from biscuit_maker.machines.machine import MachineCodes, Machine

# machine = Machine()
# print("Switch is OFF")
# state = [
#     Biscuit.NONEXISTENT,
#     Biscuit.NONEXISTENT,
#     Biscuit.NONEXISTENT,
#     Biscuit.NONEXISTENT,
#     Biscuit.NONEXISTENT,
#     Biscuit.NONEXISTENT,
#     Biscuit.NONEXISTENT,
#     Biscuit.NONEXISTENT,
# ]

def main():
    """
    sets up main threads
    """
    the_queue = Queue()
    the_queue.empty

    the_input = threading.Thread(target=input_loop, args=(the_queue,))
    the_bisquit = threading.Thread(target=main_loop, args=(the_queue,))

    the_input.start()
    the_bisquit.start()
    the_queue.join()


def input_loop(the_queue):
    """Checks for user input and puts it into the queue"""
    while True:
        user_command = input().strip().lower()
        the_queue.put(user_command)


def main_loop(the_queue):
    machine = Machine()
    while True:
        user_command = ""
        try:
            user_command = the_queue.get_nowait()
        except:
            pass

        if user_command:
            if user_command == "on":
                machine.send_signal(MachineCodes.ON)
                print("Switch is ON")
            elif user_command == "off":
                machine.send_signal(MachineCodes.OFF)
                print("Switch is OFF")
            elif user_command == "pause":
                machine.send_signal(MachineCodes.PAUSE)
                print("Switch is PAUSED")
        # if machine.state == MachineCodes.ON:
        #     if machine.oven_machine.current_temp < 220:
        #         machine.oven_machine.send_signal(OvenMachine.HEATING_ON)
        #     else:
        #         machine.oven_machine.send_signal(OvenMachine.HEATING_OFF)

        #     machine.extruder_machine.send_signal(state, ExtruderMachine.EXTRUDE)
        #     machine.stamper_machine.send_signal(state, StamperMachine.STAMP)
        #     machine.oven_machine.send_signal(state, OvenMachine.BAKE)
        # elif machine.state == Machine.OFF:
        #     machine.oven_machine.send_signal(state, OvenMachine.BAKE)
        time.sleep(0.1)


if __name__ == "__main__":
    pass
    try:
        main()
    except Exception as ex:
        print()