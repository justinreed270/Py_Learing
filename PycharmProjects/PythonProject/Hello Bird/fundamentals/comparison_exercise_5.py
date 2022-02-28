# if name is less than 3 characters
#   error message - must be at least 3 characters
# Otherwise if it's more than 50 characters long
#   name be a maximun of 50 characters
# Otherwise
#   name looks good!

#name="Casey" *20
#name="Kc"
name="Casey"
min=3
max=50
sh="The name must be"
sh2="character long."

def main():
    if len(name) <min:
        print(f'error: {sh} at least {min} {sh2}')
    elif len(name)>max:
        print(f'Error: {sh} less than {max} {sh2} ')
    else:
        print("Move along.")
if __name__ == '__main__':
    main()
