
def main():
    total = 0
    while True:
        try:
            num = input('Enter a number (q to quit): ')
            total += int(num)
        except KeyboardInterrupt:
            if num.lower() == 'q':
                print('Goodbye!')
                break

        except ValueError:
            if num.lower() == 'q':
                print('Goodbye!')
                exit()
            print('Integers only please. Try again.')
        else:
            print('The current total is:', total)

main()
