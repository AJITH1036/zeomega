
class A :
    def student(self) :
        print("student from class A ")

        
class B(A) :
    def student(self):
        print("Student from class B")

std = B()
std.student()