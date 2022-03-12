import random

def remove_color(the_list):
    color = random.choice(the_list)
    the_list.remove(color)
    return color

def main():
    colors = ['red', 'blue', 'green', 'orange']
    x_color = remove_color(colors)
    print(f'The removed color was {x_color}.')
    print(f'The remaining colors are: \n{colors}')

main()
