def lambo_diagnosis():
    print("""
    Dashboard Lights on
    Speedometer run
    3d Model off Lambo
 -> Fuel Low
 -> Next Service in 12 days
    Headlights on
    Radio On
    """)


def error_message():
    print("Command not recognized!!!")

Status = "Off"
while True:
    command = input(">")
    if command.upper() == "START" and Status == "Off":
        print("Engine Started...")
        lambo_diagnosis()
        Status = "On"
    elif command.upper() == "START" and Status == "On":
        print("Engine is already running, ready to go. Press ESC for Launch Control")
    elif command.upper() == "STOP" and Status == "On":
        print("Closing pump Valve...")
        print("Engine off")
        Status = "Off"
    elif command.upper() == "STOP" and Status == "Off":
        print("Engine is already off")
    elif command.upper() == "HELP":
        print("""
        Start -> Use this to start the Lambo Engine
        Stop -> Use this to stop the Lambo Engine
        Help -> Use this for help menu
        Quit -> Use this to exit remote Control
        """)
    elif command.upper() == "QUIT":
        break
    else:
        error_message()


