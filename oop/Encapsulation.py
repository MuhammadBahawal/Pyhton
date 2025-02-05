# Encapsulation is the concept of hiding the data inside a class and 
# restricting access to it. It helps in data security and controlled access to class attributes.

            # Public attributes can be accessed from inside and outside the class.
class Car:
    def __init__(self, brand, price):
        self.brand = brand 
        self.price = price  
        
car1 = Car("Toyota", 25000)

print(car1.brand)  
print(car1.price)  


#                   Protected Variables (_variable)
# Protected attributes should not be accessed directly outside the class.
# By convention, they should only be used inside the class and its subclasses.

class Car:
    def __init__(self, brand, price):
        self._brand = brand  
        self._price = price  


car1 = Car("Honda", 20000)


print(car1._brand)  
print(car1._price)  


#                 Private Variables (__variable)
# Private attributes cannot be accessed directly outside the class.


class Car:
    def __init__(self, brand, price):
        self.__brand = brand
        self.__price = price 
car1 = Car("BMW", 50000)


# print(car1.__brand)  provide error 
# print(car1.__price)  provide error

# we can access privete variables using get & set methods 

class Car:
    def __init__(self, brand, price):
        self.__brand = brand 
        self.__price = price  

    def get_price(self):
        return self.__price


    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")


car1 = Car("Mercedes", 60000)

print(car1.get_price())  
car1.set_price(65000)
print(car1.get_price()) 
