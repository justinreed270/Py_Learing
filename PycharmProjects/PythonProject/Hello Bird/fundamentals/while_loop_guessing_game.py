# build a guessing game.
# user gets 3 guesses.
#winning number = 9 [I choose to augment this and make it random from 1 to 10]
#after three guesses, message reads Sorry, you lose.

import random

def main():
    i=1
    num=random.randint(1,10)
#    num = 9
    limit = 3
    while i<=limit:
        guess= int(input("Guess: "))
        solve(guess,num,i,limit)
        i +=1

def solve(g,n,i,l):
    if g==n:
        print("Correct!")
        exit()
    elif g!=n and i ==l:
        print("Sorry, you lose!")
        print(f'The secret number is: {n}.')
    elif i==l:
        print("Sorry, you lose.")
        exit()
    else:
        return

if __name__ == '__main__':
    main()

