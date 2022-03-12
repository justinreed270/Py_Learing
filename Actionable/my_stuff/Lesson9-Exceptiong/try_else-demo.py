def square_num(): # use exception as flow control
    try:
        num = int(input('Input Integer: '))
    except ValueError:
        print('That is not an integer.')
    else:
        print(num, 'squared is', num**2)


def cube_num(): # use if as flow control
    num = input('Input Number: ')
    if num.isdigit():
        print(num, 'cubed is', int(num)**3)
    else:
        print('That is not an integer.')

# the difference:
    # one is like asking for permission
    # the other is like asking for forgiveness
