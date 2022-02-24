#take weight from user convert it from one unit to the other 
#display conversion weight in terminal

lbs_to_kg=0.45
kg_to_lb=2.2046

#gater input from user about weight
def what_is_weight():
    global weight
    global unit
    weight= input("Weight: ")
    unit= input("(l)lbs or (k)kg: ")
    return unit

# Convert one unit to the other
def convert():
    if unit.upper() =="L": ### RV
#   convert pounds to kilo
        x = int(weight) * lbs_to_kg
        print(f'you weigh {x} kg.')
    elif unit.upper() == "K": ### RV
#   convert kilo to Pounds
        x = int(weight) * kg_to_lb
        print(f'you weigh {x} lbs.')

def main():
    what_is_weight()
    convert()

if __name__ == '__main__':
    main()
