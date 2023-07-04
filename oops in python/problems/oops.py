class MyClass :
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def __str__(self) :
        return f"user name is {self.name} ({self.age})" 

person = MyClass("Ajith",25)


# print(person.name,person.age)
# print(person)



# Encapsulation
class car :

    __speed = 0
    __brand = ""
    
    def __init__(self) :
        self.__brand = 'Audi'
        self.__speed = 200
        self.__carbrand()
        self.__maxSpeed()


    def __maxSpeed(self) :
        print("max Speed is " + str(self.__speed))


    def __carbrand(self):
        print("Brand name is " + self.__brand)

    def details(self):
        print("car details")    
 

c = car()
# c.details()

# method overriding
class A :
    def welcome(self) :
      print("Iam from class A")

class B(A):
    def welcome(self):
     print("Iam from class B")

c = B()
c.welcome()



# polymorphism

class cat :

    def sound(self):
        print ("meow meow")

class dog :

    def sound(self) :
        print("barks")

def makeSound(animalType):
    animalType.sound()      

c = cat()
d = dog()


makeSound(c)
makeSound(d)
    


        


