
#Person - class
    #-name (attribute)
    #-talk() - (method)

class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f'Hi! I am {self.name}.')


John = Person("John Smith")
print(John.name)
John.talk()

Brittany = Person("Brittany Reed")
Brittany.talk()
