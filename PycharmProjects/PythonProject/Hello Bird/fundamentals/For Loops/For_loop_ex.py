#add the total costs of all the items in a shopping cart.
import math
# given info: (list of prices)
prices = [10,20,30]
a = 0
#my_solution
for item in prices:
    a = a + item
print(f'toatl: {a}')
