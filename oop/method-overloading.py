#meethod overloding is in a class  many functions with same name but different parameters 
# In Python, when multiple methods with the same name exist, only the last method is retained
# , and the previous ones get overridden.

class Maarks():
    def sum(self,a,b):
        print(a+b)
        
    def sum(self,a,b,c=10):
        print(a+b+c)
        
    def sum(self,c,d,e,f):
        print(c+d+e+f)
        
myobj = Maarks()
myobj.sum(2,3,4,5)
