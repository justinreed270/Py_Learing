import random

def main():
    the_list = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(the_list)
    user_choice = input("1 for Rock, 2 for Paper, 3 for Scissors: ")

    print(f'Computer: {computer_choice}')
    if user_choice =="1":
        print(f'User: {the_list[0]}')
    elif user_choice == '2':
        print(f'User: {the_list[1]}')
    elif user_choice == '3':
        print(f'User: {the_list[2]}')
    else:
        input("I do not understand, We will play again! "
              "Press Enter to continue.")
        main()


main()
