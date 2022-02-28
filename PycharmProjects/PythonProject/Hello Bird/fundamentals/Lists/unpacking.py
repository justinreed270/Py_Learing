
coordinates =(1, 2, 3)
#just too long
#coordinates [0]*coordinates[1]*coordinates[2]

#better:
#x = coordinates[0]
#y = coordinates[1]
#z = coordinates[2]

#unpacking - same result with less code
# use with list as aswell
x,y,z = coordinates
