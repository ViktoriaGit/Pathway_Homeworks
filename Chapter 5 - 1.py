import random

dice = int(input("How many dice shall we roll? "))
sum_of_numbers = 0

for i in range(dice):
    roll = random.randint(1, 6)
    sum_of_numbers += roll

print(f"\nThe sum of dice after the roll is {sum_of_numbers}")