#The car game.
status = "off"
while True:
    import time
    from Lamborghini import Lambo
    command = input(">")
    if command.upper() == "START" and status == "off":
        print("Opening Fuel Valves")
        time.sleep(3)
        print("Engine On")
        print("Running Diagnostics")
        time.sleep(4)
        Lambo.lambo_diagnosis()
        status = "on"
    elif command.upper() == "START" and status == "on":
        print("Engine is already running. Switch on Launch Control? ")
    elif command.upper() == "STOP" and status == "on":
        print("Engine Off")
        status = "off"
    elif command.upper() == "STOP" and status == "off":
        print("Engine is already off")
    elif command.lower() == "help":
        print(
            """
            help 1
            help 2
            help 3
            """
        )
    else:
        print("Invalid Command")



















"""
from Lamborghini import Lambo
status = "Off"
while True:
    handle = input("-->")
    if handle.upper() == "START" and status == "Off":
        Lambo.lambo_diagnosis()
        status = "On"
    elif handle.upper() == "START" and status == "On":
        print("Engine already running. Do you want launch control instead? ")
    elif handle.lower() == "stop" and status == "On":
        print(
        Closing Valves...
        Closing Fuel Pump...
        Stopping Engine...
        Engine Off
        )
        status = "Off"
    elif handle.lower() == "stop" and status == "Off":
        print("Engine is already off")
    elif handle.upper() == "HELP":
        print(
            #START -> To start Engine
            #STOP -> To stop Engine
            #HELP -> For car command manual
            #QUIT -> To quit game.
            
    elif handle.upper() == "QUIT":
        break
    else:
        print("Invalid command")
"""
















'''
from Lamborghini import Lambo
status = "Off"
while True:
    handle = input("-->")
    if handle.upper() == "START" and status == "Off":
        Lambo.lambo_diagnosis()
        status = "On"
    elif handle.upper() == "START" and status == "On":
        print("Engine is already running, would you like to engage Launch Control?")
    elif handle.lower() == "stop" and status == "On":
        print("""
        Closing valves
        Closing fuel pump
        Engine Off.
        """)    
        status = "Off"
    elif handle.lower() == "stop" and status == "Off":
        print("Engine already off")
    elif handle.upper() == "HELP":
        print("""
            #START -> To start Engine
            #STOP -> To stop Engine
            #HELP -> For car command manual
            #QUIT -> To quit game.
            """)        
    elif handle.upper() == "QUIT":
        break
    else:
        print("Invlid Command!")
'''
