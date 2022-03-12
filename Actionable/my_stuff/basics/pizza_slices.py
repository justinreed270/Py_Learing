import math

x=1
import math

ppl_eating= input("How many people are eating? ")
slice_per_person = input("How many slices per person? ")
slice_per_pie = input("How many slices per pie? ")

slices_needed = int(ppl_eating) * math.ceil(float(slice_per_person))
pies = int(slices_needed) / int(slice_per_pie)
total_pies = math.ceil(pies)
leftovers = int(slices_needed) % int(slice_per_pie)


print(f'You need {total_pies} pizza(s) to feed {ppl_eating} people.\n'
      f'There will be {leftovers} slices leftover.')
