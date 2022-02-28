#10 = int
#10.1 = float

#with all operators below,there is an augmented assignment operator


def main():
    print(10 +3)
    print(10*3)
    print(10-3)
    print(10/3)
    print(10//3)
    print(10%3) #modulous returns the remainder of the division
    print(10 ** 3) # power

def incrumently_chng_a_num():
    x=10
    x=x+3
    print(x)

def augmented():
    x=10
    x += 3 #augmented assignment operator
    print(x)
if __name__ == '__main__':
 #   main()
    incrumently_chng_a_num()
    augmented()
