class Land :
    def land(self,name) :
        self.name = name
        print(f"{name} lives on land")

class  Water :
    def water(self,name) :
        print(f"{name} lives in water")  

class Animal(Land,Water) :
          pass
      
a  = Animal()     
a.land("frog")
a.water("frog")