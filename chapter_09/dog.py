class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        """Simulate rolloing over in response to a command."""
        print(f'{self.name} rolled over!')


my_dog = Dog('Willie', 6)
dog_2 = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"My dog's name is {dog_2.name}.")
print(f"My dog is {dog_2.age} years old.")
dog_2.sit()
dog_2.roll_over()
