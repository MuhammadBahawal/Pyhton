class student :
   
   
    sub = "BSSE"
# instance method
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
        print(f"My name is {name} and my age is {age} ")
        


# class methods
    @classmethod
    def clas_method(cls):
        print(f"and my class is {cls.sub}")


# static method
    @staticmethod
    def hello():
        print("Hello Students how are you: ")



myobj = student("M.Bahawal",20)
myobj.clas_method()
myobj.hello()