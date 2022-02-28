# practice: find the largest item in a list

numbers=[1,2,3,8989,4,5,87]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)
