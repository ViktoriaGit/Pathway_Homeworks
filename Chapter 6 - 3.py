def gallons_to_liters(gallons):
    return gallons * 3.785

while True:
    input_gallons = float(input("Enter gallons (negative to quit): "))
    if input_gallons < 0:
        break

    liters = gallons_to_liters(input_gallons)
    print(f"{input_gallons} gallons is {liters:.2f} liters.")