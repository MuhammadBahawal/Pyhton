class parent():
    
    @staticmethod
    def Hello():
        print("hello this is a parent class method :")
        
class child(parent):
    @staticmethod
    def Hello():
        print("Hello this is child method :")

myobj = child()

myobj.Hello()