class Dog:
    def sound(self) :
        print("Bow Bow")

class Cat :
    def sound(self) :
        print("Meow meow")

def MakeSound(animalType) :
    animalType.sound()   

c = Cat()
d = Dog()

MakeSound(c)
MakeSound(d)