# write the divide() function

def divide(numerator,denominator):
    floor = numerator//denominator
    remainder  = numerator % denominator
    print(f'{numerator} divided by {denominator}'
          f' is {floor} with a remainder of {remainder}.')
def main():
    divide(5, 2)
    divide(6, 3)
    divide(12, 5)
    divide(1, 2)

main()
