# Duck Typing is a concept in Python where an object's behavior (i.e., the methods and attributes it has)
# is more important than its actual type or class. If an object has the necessary methods,
# it can be used in place of another type without needing to explicitly check its class.


class Bird:
    def fly(self):
        print("Bird is flying")


class Airplane:
    def fly(self):
        print("Airplane is flying")


class Rocket:
    def fly(self):
        print("Rocket is launching into space!")


def lift_off(obj):
    obj.fly()
    
bird = Bird()
airplane = Airplane()
rocket = Rocket()


lift_off(bird)
lift_off(airplane)
lift_off(rocket)
