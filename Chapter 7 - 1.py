seasons = ("winter", "spring", "summer", "autumn")
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
month = int(input("Enter the number of the month (1-12): "))


if month == 12 or month == 1 or month == 2:
    season = seasons[0]
elif 3 <= month <= 5:
    season = seasons[1]
elif 6 <= month <= 8:
    season = seasons[2]
elif 9 <= month <= 11:
    season = seasons[3]
else:
    season = "invalid"

if season != "invalid":
    print(f"\n{months[month-1]} is in the {season}.")
else:
    print("\nThat is not a valid month number. Please enter a number between 1 and 12.")
