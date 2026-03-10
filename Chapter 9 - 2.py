class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0

new_car = Car("ABC-123", 142)

print(f"Registration: {new_car.registration_number}")
print(f"Max Speed: {new_car.max_speed} km/h")
print(f"Current Speed: {new_car.current_speed} km/h")
print(f"Distance: {new_car.travelled_distance} km")

new_car.accelerate(30)
print(f"Speed after increases: {new_car.current_speed} km/h")
new_car.accelerate(70)
print(f"Speed after increases: {new_car.current_speed} km/h")
new_car.accelerate(50)
print(f"Speed after increases: {new_car.current_speed} km/h")
new_car.accelerate(-200)
print(f"Speed after emergency brake: {new_car.current_speed} km/h")
