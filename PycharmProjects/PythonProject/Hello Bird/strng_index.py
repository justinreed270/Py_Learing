#indexing string data type

course="Python course for beginners"
#index= 0123456...
other = course[:]

def main():

    print(course[0])
    print(course[-1])
    print(course[0:3]) #excludes index3
    print(course[0:])
    print(course[1:])
    print(course[:5])
# clone a string
    print(course[:])
    print(other)
    print(course[1:-1])
if __name__ == "__main__":
    main()
