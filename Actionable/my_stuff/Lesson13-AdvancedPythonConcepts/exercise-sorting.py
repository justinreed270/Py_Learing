# Simple sort() method
colors = ['red', 'blue', 'green', 'orange']
print(f'Before: {colors}')
# colors.sort()
new_colors = sorted(colors) # This one has been done for you
print(new_colors)

# The reverse argument:
#colors.sort(reverse=True)
new_colors2 = sorted(colors, reverse=True)
print(new_colors2)

# The key argument:
#colors.sort(key=len)
new_colors3 = sorted(colors, key=len)
print(new_colors3)


# The key argument with named function:
def get_lastname(name):
    return name.split()[-1]


people = ['George Washington', 'John Adams',
          'Thomas Jefferson', 'John Quincy Adams']
print(f'as is: {people}')
#people.sort(key=get_lastname)
people1 = sorted(people, key=get_lastname)
print(people1)

# The key argument with lambda:
#people.sort(key=lambda name: name.split()[-1])
people2 = sorted(people, key=lambda name: name.split()[-1])
print(people2)

# Combing key and reverse
#colors.sort(key=len, reverse=True)
colors4 = sorted(colors, key=len, reverse=True)
print(colors4)
