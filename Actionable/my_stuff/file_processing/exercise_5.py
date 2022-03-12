with open("1880-boys.txt") as f:
    boys = f.read()

with open("1880-girls.txt") as f:
    girls = f.read()

with open("my_file2.txt", "a") as f:
    f.write(f'\n Boys: \n {boys} \n Girls: \n {girls}')
