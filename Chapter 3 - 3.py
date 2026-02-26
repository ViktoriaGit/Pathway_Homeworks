gender = input("Enter biological gender (male/female): ")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("\nYour hemoglobin value is low.")
    elif hemoglobin > 155:
        print("\nYour hemoglobin value is high.")
    else:
        print("\nYour hemoglobin value is normal.")

elif gender == "male":
    if hemoglobin < 134:
        print("\nYour hemoglobin value is low.")
    elif hemoglobin > 167:
        print("\nYour hemoglobin value is high.")
    else:
        print("\nYour hemoglobin value is normal.")

else:
    print("\nYou have not entered a valid biological gender.")