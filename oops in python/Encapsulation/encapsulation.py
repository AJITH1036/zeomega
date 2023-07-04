class car :

    __speed = 0
    __name = ""

    def __init__(self) :
       self.__speed = 200
       self.__name = "Audi"
       self.__maxSpeed()
    

    def __maxSpeed(self):
        print("maximum speed is "  + str(self.__speed))

    def name(self) :        
        print("Car name is "+ self.__name)    

c = car()

c.name()




