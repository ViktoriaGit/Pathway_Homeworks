import math

def unit_price(diameter_cm, price_euro):
    radius_m = (diameter_cm / 2) / 100
    area_m2 = math.pi * (radius_m ** 2)
    return price_euro / area_m2


dia1 = float(input("Enter diameter of Pizza 1 (cm): "))
price1 = float(input("Enter price of Pizza 1 (€): "))


dia2 = float(input("Enter diameter of Pizza 2 (cm): "))
price2 = float(input("Enter price of Pizza 2 (€): "))

unit_price1 = unit_price(dia1, price1)
unit_price2 = unit_price(dia2, price2)

print(f"\nPizza 1 unit price: {unit_price1:.2f} €/m²")
print(f"Pizza 2 unit price: {unit_price2:.2f} €/m²")

if unit_price1 < unit_price2:
    print("Pizza 1 offers better value.")
elif unit_price2 < unit_price1:
    print("Pizza 2 offers better value.")
else:
    print("Both pizzas have the same value.")