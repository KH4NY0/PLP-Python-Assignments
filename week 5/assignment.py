class Smartphone:

    def __init__(self, brand, model, color, battery_percentage):
        self.brand = brand
        self.model = model
        self.color = color
        self.__battery_percentage = battery_percentage  # Encapsulation for battery percentage (private)

    # Method to simulate making a call
    def make_call(self, number):
        print(f"Calling {number}...")

    # Method to simulate sending a message
    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    # Method to simulate charging the phone
    def charge_phone(self, charge_amount):
        self.__battery_percentage = min(100, self.__battery_percentage + charge_amount)  # Ensure battery does not exceed 100%
        print(f"Charging... Battery is now at {self.__battery_percentage}%")

    # Implementing a getter method for battery percentage
    def get_battery(self):
        return self.__battery_percentage

    # Implementing a setter method for battery percentage with validation
    def set_battery(self, value):
        if 0 <= value <= 100:
            self.__battery_percentage = value
        else:
            print("Battery percentage must be between 0 and 100.")

    # Display phone details
    def display_info(self):
        print(f"Smartphone Info - Brand: {self.brand}, Model: {self.model}, Color: {self.color}, Battery: {self.__battery_percentage}%")

# Creating an instance of the Smartphone class
my_phone = Smartphone("Apple", "iPhone 13", "Space Gray", 75)

# Calling methods on the object
my_phone.display_info()
my_phone.make_call("123-456-7890")
my_phone.send_message("123-456-7890", "Hey, what's up?")
my_phone.charge_phone(20)
my_phone.set_battery(50)

# Displaying the current battery level
print(f"Current battery: {my_phone.get_battery()}%")
