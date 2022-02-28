# len() count stg - general purpose function
#   one way to use this is to ensure text limits for fields on a webpage

#specifiv functions specifically designed for the str type
#   these are refered to as method
#var.upper()
#var.lower()
#var.find('<letter or letters to find>')
#var.replace('<word(s) to replace>', '<what to change it to>')
# "in" (operator)produces a bulian value


#use the Dot "." to show functions/methods
course="Python for beginners"

def main():
    print(course.upper())
    print(course.lower())
    print(len(course))
    print(course.find('P'))
    print(course.replace('Python', 'Bird watching'))
    print("Python" in course)

if __name__ == '__main__':
    main()
