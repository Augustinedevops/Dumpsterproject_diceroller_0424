import random

class Dice:
    def roll1(self):
        return random.randint(1,6)
    def roll2(self):
        return random.randint(1,6)


dice=Dice()

result1=dice.roll1()
result2=dice.roll2()

print( result1,result2)

