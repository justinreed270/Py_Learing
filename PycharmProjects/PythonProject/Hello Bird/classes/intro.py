
# Classes can be used to define new types to model real world concepts
#class examples:
    #Number
    #String
    #Boolean
    #___
    #Lists
    #Dictionaries
#real world concepts for class:
    # what is in the cart

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


#Point() - creates a new object
#point1 - variable of stored object
#the object is called point1
point1 = Point()
point1.x =10 #creating an atribute
point1.y =20
point1.draw() #calling the draw method of the Point() object

#creating second object - called - point2
#each object is a different instance of the Point() class.
point2 = Point()
point2.x = 1
print(point2.x)
