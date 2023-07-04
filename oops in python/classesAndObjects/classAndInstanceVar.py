class student :
    college = "ABC"

    def __init__(self,name,department) :
        self.name = name
        self.department = department

    def display(self) :
        print("Name : " + self.name)
        print("Department " + self.department)
        print("College : " + student.college)
 
student1 = student("Ajith","Mech")
student2 = student("Manoj","EEE")


students = [student1,student2]
 
for x in students :
    x.display()



    