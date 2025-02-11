# A decorator is a function that modifies another
# function without changing its code. It uses the @decorator_name syntax.

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
say_hello()
