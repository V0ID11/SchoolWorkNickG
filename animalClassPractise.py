class Animal:
    def __init__(self, gender, type, sound, name, home, foodType):
        self.gender = gender
        self.type = type
        self.sound = sound
        self.name = name
        self.home = home
        self.foodType = foodType
    def speak(self):
        return self.sound
    def consume(self):
        print(f"Being a {self.type} {self.name} devours {self.foodType}, {self.name} says {self.speak()}")
    def goHome(self):
        print(f"{self.name} has retreated to his {self.home}")

harry = Animal("Male", "Cat", "Meow", "harry", "House", "Cat Food")
samL = Animal("Female", "Dragon", "Meow" , "Sam Lockie", "Lair" , "Nick")
print(samL.speak())
samL.consume()
samL.goHome()