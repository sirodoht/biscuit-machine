machine = Machine()
print("Switch is OFF")
state = [
    Biscuit.NONEXISTENT,
    Biscuit.NONEXISTENT,
    Biscuit.NONEXISTENT,
    Biscuit.NONEXISTENT,
    Biscuit.NONEXISTENT,
    Biscuit.NONEXISTENT,
    Biscuit.NONEXISTENT,
    Biscuit.NONEXISTENT,
]

while True:
    user_command = input().strip().lower()

    if user_command == "on":
        machine.send_signal(Machine.ON)
        print("Switch is ON")
    elif user_command == "off":
        machine.send_signal(Machine.OFF)
        print("Switch is OFF")
    elif user_command == "pause":
        machine.send_signal(Machine.PAUSE)
        print("Switch is PAUSED")

    if machine.state == Machine.ON:
        machine.extruder_machine.send_signal(state, ExtruderMachine.EXTRUDE)
        machine.stamper_machine.send_signal(state, ExtruderMachine.STAMP)
        machine.oven_machine.send_signal(state, ExtruderMachine.BAKE)
