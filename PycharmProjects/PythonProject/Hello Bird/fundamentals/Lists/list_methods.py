numbers=[5,3,2,1,5,4, 5,7]
numbers2 = numbers.copy()
numbers.append(11)
print(numbers)

numbers.insert(1,78)
print(numbers)

numbers.remove(5)
print(numbers)

#numbers.clear()
#print(numbers)

#removes the last index
numbers.pop()
print(numbers)

#check for the existance of an item in the list
print(numbers.index(5))

#Check for existance - get an error
#print(numbers.index(50))

#check for existance - bulian value (safer)
print(50 in numbers)

#count the number 
print(numbers.count(5))

#returns none-
print(numbers.sort())

#sort this way:
numbers.sort()
numbers.reverse()
print(numbers)

#copy
# see second var above
print(numbers)
print(numbers2)
