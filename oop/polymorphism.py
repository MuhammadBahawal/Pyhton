# The same function name can have different behaviors across different classes.

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):  # Overriding parent method
        print("Child method")

c = Child()
c.show()  # Output: Child method
