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
        print("""
        Closing Valves...
        Closing Fuel Pump...
        Stopping Engine...
        Engine Off
        """)
        status = "Off"
    elif handle.lower() == "stop" and status == "Off":
        print("Engine is already off")
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
        print("Invalid command")

















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
