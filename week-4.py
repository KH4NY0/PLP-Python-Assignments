class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am a {self.gender}.")

x = input('Enter your name: ')

while True:
    try:
        y = int(input("Enter your age: "))
        break  # Exit the loop if the input is valid
    except ValueError:
        print("Invalid input. Please enter a numeric value for your age.")

z = input('Enter your gender: ')

person = Person(name = x, age = y, gender = z)

person.introduce()
