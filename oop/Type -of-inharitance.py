#                     Single Inheritance
# Single inheritance occurs when a class inherits from one parent class.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal): 
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  
dog.bark()  

#                         Multiple Inheritance
# Multiple inheritance occurs when a class inherits from multiple parent classes.

class Animal:
    def speak(self):
        print("Animal speaks")

class Flyable:
    def fly(self):
        print("Flying!")

class Bat(Animal, Flyable):  
    def sound(self):
        print("Screech!")

bat = Bat()
bat.speak() 
bat.fly()  
bat.sound()  


#                   Multilevel Inheritance
# Multilevel inheritance is when a class inherits from a class 
# that already inherits from another class. In other words, it forms a "chain" of inheritance.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  
    def bark(self):
        print("Dog barks")

class Puppy(Dog):  
    def whine(self):
        print("Puppy whines")

puppy = Puppy()
puppy.speak()  
puppy.bark()   
puppy.whine() 

                    # Hierarchical Inheritance
# In hierarchical inheritance, multiple classes inherit from a single parent class.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Inherits from Animal
    def bark(self):
        print("Dog barks")

class Cat(Animal):  # Inherits from Animal
    def meow(self):
        print("Cat meows")

dog = Dog()
dog.speak()  # Inherited from Animal
dog.bark()   # Defined in Dog

cat = Cat()
cat.speak()  # Inherited from Animal
cat.meow()   # Defined in Cat
