# Used to check if two variables point to the same object in memory


a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True (Same object)
print(a is c)  # False (Different objects with same values)
print(a == c)  # True (Same values)
