
### must explicitly close the file
#f = open("notes.txt")
#contents = f.read()
#print(contents)
#f.close()


#python automatically closes
with open("notes.txt") as f:
    contents = f.read()
    print(contents)
