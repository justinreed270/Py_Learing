
#write a program to remove the duplicates in a list.

numbers = [1, 1 ,2 ,2 ,3 ,3 ,4 ,4 ,5 ,6 ,7 ,8 ,1 ,3 ,4 ,2]
###########
test = numbers[0]
for item in numbers:
    if numbers.count(item) >1:
        numbers.remove(item)
print(numbers)
###########
#Mosh

uniques = []
for number in  numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
