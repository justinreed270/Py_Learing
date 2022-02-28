

def find_max(number):
    biggest = number[0]
    for number in number:
        if number > biggest:
            biggest = number
    return biggest


