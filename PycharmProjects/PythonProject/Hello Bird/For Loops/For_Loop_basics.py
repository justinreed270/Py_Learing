# For loop - iterate over items of a collection
def A():
    for item in 'Python':
        print(item)

# use a list with []
def B():
    for item in ['Jason', 'Terry', 'Justin']:
        print(item)

def C():
    for item in [1,2,3,4]:
        print(item)
# large list of numbers
def D():
#    for item in range(10):
#    for item in range(5,10):
    for item in range(5,10, 2):   # use a step function
        print(item)
D()
