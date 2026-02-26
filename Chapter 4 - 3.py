numbers = []

while True:
    given_numbers = input("Enter a number (press Enter to quit): ")
    if given_numbers == "":
        break
    else:
        numbers.append(float(given_numbers))
numbers.sort()

if len(numbers) > 0:
    print (f"The smallest number is: {numbers[0]}")
    print(f"The largest number is: {numbers[-1]}")
else:
    print("You didn't enter any numbers")