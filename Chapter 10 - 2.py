class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom = bottom_floor
        self.top = top_floor

        self.elevators = []
        for i in range(number_of_elevators):
            new_elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(new_elevator)

    def run_elevator(self, elevator_nr, destination):
        chosen_elevator = self.elevators[elevator_nr]

        print(f"\nMoving elevator number {elevator_nr} to floor {destination}")
        chosen_elevator.go_to_floor(destination)


print("\nTesting Building with Elevators")
office = Building(1, 12, 3)
office.run_elevator(0, 8)
office.run_elevator(1, 4)

