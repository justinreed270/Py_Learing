
# many applications in data science and machine learning

#3X3 matrix in math
#[
#    1 2 3
#    4 5 6
#    7 8 9
#]

#model above in a 2d list
# each item in list is another list
matrix = [
    [1,2,3], # represents items in first row
    [4,5,6], # 2nd row
    [7,8,9]  #3rd row
]

# How to access list:
print(matrix[0][1])

matrix[0][1] = 20
print(matrix[0][1])

#iterate 
for row in matrix:
    for item in row:
        print(item)
