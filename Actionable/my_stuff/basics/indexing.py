def main():
    phrase = input("What is your phrase? ")
    print(f'Your phrase is: \'{phrase}\'.', sep=" ")
    select= int(input("Which charater? [Enter a number] "))
    print(f'Character {select} is {phrase[select - 1]}')


main()
