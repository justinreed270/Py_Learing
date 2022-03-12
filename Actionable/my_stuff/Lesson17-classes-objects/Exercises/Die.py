from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
        
    # add a roll() method
    def roll(self):
        roll = randint(1, self.sides)

        return roll


def main():
    jane_die = Die
    print(roll(jane_die))
    print('end')


if __name__ == '__main__':
    main()
