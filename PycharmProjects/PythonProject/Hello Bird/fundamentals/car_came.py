
# car start game
#when you run the game:
# get symbol ">"
# "help" gives you: (non case sinsitive)
# '''start - to start the car
# stop - to stop the car
#quit - to exit '''
# any other commands "I do not understand that..."
# when user types:
# input "start"
# output "Car started... Ready to go!"
#input "stop"
#output "Car stopped."
#input "quit"
# program stops
def variable():
    command=input(">")
    return command

def help():
    print(f'start - to start the car')
    print(f'stop - to stop the car')
    print(f'quit - to exit')
    main()

def start():
    print(f'Car started...Ready to go!')
    main()

def stop():
    print(f'Car stopped')
    main()

def quit():
    print("Thanks for playing the Car Game, bye!")
    exit()

def hmm():
    print('I do not understand...')

def main():
    command= variable()
    me = command.lower()
 #   p = True
#    while p == True:
    if me=="start":
        start()
    elif me == "stop":
        stop()
    elif me == "quit":
        quit()
    elif me== "help":
        help()
    else:
        hmm()
        e= input('Would you like to keep playing? y/n: ')
        if e.lower()=='y':
            main()
        elif e.lower()=='n':
            quit()
        else:
            hmm()
            print('I am confused, lets take it from the start.')
            main()

if __name__ == '__main__':
    main()
