# The super() function allows the child class to call the overridden method from the parent class.


class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Cat(Animal):
    def make_sound(self):
        super().make_sound()  # Calling parent method
        print("Cat says Meow!")

# Creating an object
cat1 = Cat()
cat1.make_sound()
