# programming with Mosh - solutions

command =""
#while command != "quit":
while True:
    command = input('> ').lower() # call methods once make for cleaner code
    if command  == 'start':
        print('Car started.')
    elif command == "stop":
        print('Cart Stopped.')
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
