import random

def custom_dice(sides):
    return random.randint(1, sides)

max_sides = int(input("How many sides does the dice have? "))
result = 0
roll = 0

while result != max_sides:
    result = custom_dice(max_sides)
    roll +=1
    print(f"Roll {roll}: {result}")