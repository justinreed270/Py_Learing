#Price of a house is $1M
#If buyer has good credit,
#   they need to down 10%
#otherwise
#    they need to put down 20%
#Print the down payment for a buyer with good credit
price=1000000
is_good_credit=False
percent=.1

def main():
    print(f'Pay em good: {payment()}')

def payment():
    if is_good_credit:
        return (price*percent)
    else:
        return(price*(percent*2))

if __name__ == '__main__':
    main()
