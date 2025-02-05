# Inheritance allows a class (child class) to inherit properties and methods
# from another class (parent class). This helps in code reuse and extensibility.


class teacher():
    Name = "Adeel"
    age = 20
    
    @staticmethod
    def sum(a,b):
        print(a+b)
    
    
class student(teacher):
    @staticmethod
    def hello():
        print("hello how are you ")
        

myobj = student()

myobj.sum(4,5)