# formatted strngs are useful when you want to dynamically
#create some text with your variables.


#you want to print the following to the terminal
#John [Smith] is a coder

first_name="John"
last_name="Smitn"

#complicated:
message= first_name + ' [' + last_name + '] is a coder'
#formatted:
# f and {} for dynamically inserting value into strng
msg= f'{first_name} [{last_name}] is a coder'

def main():
    print(message)
    print(msg)

if __name__ == '__main__':
    main()
