# tell the user
#If its hot
#   Its a hot day.
#   Dink plenty of water
#If its a cold day
#   Tt's a cold day.
#   Wear warm clothes
#otherwise
# It's a nice day.

is_hot=False
is_cold=False

def main():
    if is_hot:
        print("It's a hot day.")
        print("Drink plenty of water.")
    elif is_cold:
        print("It's a cold day.")
        print("Wear warm clothes.")
    else:
        print("It's a nice day.")
    print("Have a nice day.")

if __name__ == '__main__':
    main()
