#A closure is a function that remembers variables from
# its enclosing scope even after the scope has finished executing. 
def outer_function(x):
    def inner_function():
        print(f"Value of x is: {x}")  # Inner function remembers 'x'
    return inner_function  # Returning the inner function

# Creating a closure
closure_func = outer_function(10)

# Calling the closure function
closure_func()  # Output: Value of x is: 10
