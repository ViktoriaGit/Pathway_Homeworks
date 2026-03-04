import random

def dice():
    return random.randint(1, 6)

result = 0
roll = 0
while result != 6:
    result = dice()
    roll +=1
    print(f"Roll {roll}: {result}")