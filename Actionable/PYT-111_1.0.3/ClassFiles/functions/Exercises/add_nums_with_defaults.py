
# def add_nums(num1, num2, num3, num4, num5):
#     total = num1 + num2 + num3 + num4 + num5
#     print(num1, '+', num2, '+', num3, '+', num4, '+', num5, ' = ', total)
#
# def main():
#     add_nums(1, 2, 0, 0, 0)
#     add_nums(1, 2, 3, 4, 5)
#     add_nums(11, 12, 13, 14, 0)
#     add_nums(101, 201, 301, 0, 0)


def add_nums(num1, num2, num3=0, num4=0, num5=0):
    total = num1 + num2 + num3 + num4 + num5
    #print(num1, '+', num2, '+', num3, '+', num4, '+', num5, ' = ', total)
    return total


def main():
    # add_nums(1, 2,)
    # add_nums(1, 2, 3, 4, 5)
    # add_nums(11, 12, 13, 14)
    # add_nums(101, 201, 301)
    result = add_nums(1,2)
    print(result)
    result=add_nums(result, 3)
    print(result)


main()
