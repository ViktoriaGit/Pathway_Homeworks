while True:
    inches = float(input("Enter inches (a negative number will end the program): "))

    if inches < 0:
        print("Program ended.")
        break
    print(f"That is {inches*2.54:.2f} centimeters.")