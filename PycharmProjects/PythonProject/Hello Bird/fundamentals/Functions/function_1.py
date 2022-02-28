def greet_user(first,last):#parameters
    print(f'Hi {first} {last}.')

greet_user(last="Smith", first="John") #key word argument
greet_user("John", "Smith") # positional arguments
greet_user("John", last="Smith")
greet_user("John",)
