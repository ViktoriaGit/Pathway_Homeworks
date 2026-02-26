numbers = []

while True:
    num = input("Enter a whole number (press Enter to quit): ")

    if num == "":
        break
    else:
        number = int(num)
        numbers.append(number)

numbers.sort(reverse=True)
print(f"\nThe five greatest numbers are: {numbers[:5]}")