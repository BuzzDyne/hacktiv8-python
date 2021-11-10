class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound="Guk"):
        return f"{self.name} says '{sound}'"

    def showOff(self):
        print("\n========  Dog is showing off  =======")
        print(f"Name\t: {self.name}\nAge\t: {self.age}\nSpecies\t: {self.species}")
        print(f'desc method\t: {self.description()}\nspeak method\t: {self.speak(f"Hello there, my name is {self.name}")}')

class Pom(Dog):
    def speak(self, sound="WOI"):
        return f"I'm Dog 2.0, a Pom! This is my message: '{sound}'"

# if __name__ == '__main__':

coco = Dog("Coco", 1)
coco.showOff()
dooo = Dog("dooo", 2)
dooo.showOff()
eman = Dog("eman", 3)
eman.showOff()

pom = Pom("Child Pom", 2)
pom.showOff()