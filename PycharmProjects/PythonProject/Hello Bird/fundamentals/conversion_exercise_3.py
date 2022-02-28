#Exercise 3
#Ask the user weight (in pounds), convert it to kilograms, print on terminal.
#to convert pounds to kilograms
# divide pounds by 2.2046

user_lbs = input("How much do you weight in pounds? ")
lbs_kilogram_conversion=2.2046

def main():
    user_kg = int(user_lbs) / lbs_kilogram_conversion
    print("You weigh " + str(user_kg) + "kg.")
    var1= int(user_lbs) * 0.45
    print(var1)

main()
