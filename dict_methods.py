student = {
    "name":"M.Bahawal",
    "Roll_No":239,
    "class":"BSSE"
}
#method for checking the itmes in the dictionary is item()

print(student.items())

# for getting the keys of the dictionary use .key()
print(student.keys())

#we use .value() for getting the value of the dictionary
print(student.values())

#use update for updating the value
print(student.update({"name":"Adeel"}))
print(student)

# use .get() method for getting the values of the key 
print(student.get("name"))

# .clear method use to clear the dictionary 
# student.clear()
# print(student)

# .copy method use to copy the dictionary 
student.copy()
print(student)

#use to pop or remove the value from the dictionary 
student.pop("name")
print(student)

# use to remove or pop the value from last
student.popitem()
print(student)

