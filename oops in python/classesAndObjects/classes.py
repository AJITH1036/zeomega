class MyClass :
    def __init__(self,name,age) :
      self.name = name
      self.age = age
    
    def __str__(self):
       return f"User name is  {self.name}({self.age})"


p1 = MyClass('ajith',25)    
print(p1.name,p1.age)
print(p1)

