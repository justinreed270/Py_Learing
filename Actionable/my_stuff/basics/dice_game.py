import random
i=1

def roll_die(sides=6):
    global i

    while i < 4:
        num_rolled = random.randint(1,sides)
        if i == 1:
            total = num_rolled
            print(f'You rolled a {num_rolled}.')
            print(f'Total after first roll: {total}')
        elif i == 2:
            total += num_rolled
            print(f'You rolled a {num_rolled}')
            print(f'Total after {i} rolls: {total}')
        elif i == 3:
            total += num_rolled
            print(f'You rolled a {num_rolled}')
            print(f'Total after {i} rolls: {total}')
        i +=1


def main():
    roll_die()


if __name__ == '__main__':
    main()
