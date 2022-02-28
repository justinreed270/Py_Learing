
#A mechanism for reusing code

#DRY (Don't Repeat Youself)

class Dog:
    def walk(self):
        print("walk")

class Cat:
    def walk(self):
        print("walk")

#Better way below

class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal): #Dog class now takes on the Mammal methods
#    pass    #telling python to not worry
    def bark(self):
        print("bark, bark")

class Cat(Mammal):
#    pass
    def meow(self):
        print("meow")


Bailey = Dog()
Bailey.walk()
Bailey.bark()

jessi = Cat()
jessi.walk()
jessi.meow()

