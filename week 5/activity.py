# Base class Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement the move() method.")

# Subclass Car that inherits from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving")

# Subclass Plane that inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying")

# Subclass Boat that inherits from Vehicle
class Boat(Vehicle):
    def move(self):
        print("Sailing")

# Function to test polymorphism
def test_move(vehicle):
    vehicle.move()  # Calls the correct move() based on the vehicle type

# Creating instances of each vehicle
car = Car()
plane = Plane()
boat = Boat()

# Calling the move method dynamically based on the object type
test_move(car)
test_move(plane)
test_move(boat)
