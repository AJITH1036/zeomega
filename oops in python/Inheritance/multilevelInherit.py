class Student :
    def name(self) :
        print("Ajith ! Iam from parent class")

class Department(Student) :
    def department(self) :
        print("Mech ! Iam from derived class 1")

class College(Department) :
    def college(self) :
        print("ABC ! Iam from derived class 2")

studentData = College()

studentData.name()
studentData.department()
studentData.college()
