# create an "F" shape with x's.
#cheating is multiplying x by the number held in the iteration

#given:
numbers = [5,2,5,2,2]
#my_code

#cheating:
#for line in numbers:
#    a = int(line)
#    print('x' * a)
#
#for line in numbers:
 #   a = str(line)
#    for item in numbers:
#        print()
#count = 0
#for item in numbers:
#    item = str(item)
 #   for item2 in range(len(item)):
  #      print(index,item[index])
#for count, item in numbers:
#    print(item)

#Mosh's Solution:

for x_count in numbers:
    output =""
    for count in range(x_count):
        output = output + "X"
    print(output)
