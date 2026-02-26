cities = []

print("Please enter the names of five cities: ")
for i in range(5):
    city_name = input(f"Enter city {i + 1}: ")
    cities.append(city_name)

print("\nYou entered the following cities: \n")
for city in cities:
    print(city)