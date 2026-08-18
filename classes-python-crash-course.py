class Dog:
    """A simple attempt to model a dog."""

    def __init__(self,name,age,gender):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        self.gender = gender

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over! Good {self.gender}!")

my_dog = Dog('Teddy',2, 'boy')

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()