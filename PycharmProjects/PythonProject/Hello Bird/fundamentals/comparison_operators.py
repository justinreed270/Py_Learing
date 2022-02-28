#Comparison Operators are used when you want to
#   compare a variable to a value

#If the temp is more than 30
#   It's a hot day
#Otherwise if its less than 10
#   It's a cold day
#Otherwise
#   It's a nice day
# > ; < ; >= ; <= ; ==; !=
# <
#

temp= 9

def main():
    if temp > 30:
        print("It's a hod day.")
    elif temp < 10:
        print("Tt's a cold day.")
    else:
        print("It's a nice day.")
    print("Jason, have you seen my glass?")


if __name__ == '__main__':
    main()

