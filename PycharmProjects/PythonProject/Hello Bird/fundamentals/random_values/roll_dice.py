import random

class Dice:    
    # __init__(self,x):
     #   self.x = x
 #       self.y =y
      #  pass


    def roll(self,x):
        r1 =random.choice(x)
#        r2 =random.choice(y)
        return r1,


dice1 ="1", "2", "3", "3", "5", "6"
dice2 = dice1

t = ["2", "3"]
m = random.choice(t)
v  = [m]
print(m)
print(v)
play = Dice()
print(play.roll(v))
k = play.roll(m)

print(f'({k}, {k})')




