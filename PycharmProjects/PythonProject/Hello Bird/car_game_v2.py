
#Car_started=False
#Car_stopped=False
started = False
while True:
    command = input('> ').lower()
    if command  == 'start':
#        if Car_started is True:
        if started is True:
            print("Car is already started.")
        else:
            print('Car started.')
            started = True
            #Car_started = True
    elif command == "stop":
#        if Car_stopped is True:
#        if started is not True:
#        if started is False:
        if not started:
            print("Car is already Stopped.")
        else:
            print('Car Stopped.')
            started = False
#            Car_stopped = True
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)

    elif command == "quit":
        break
    else:
        print("sorry, I don't understand that")
