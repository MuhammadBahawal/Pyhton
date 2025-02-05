# list is a collection of data it is similar to array

# data = [1,2,3,4,5,6,7,"hello"]
# print(data)

# print(data[0])
# print(data[2:6]) #required limited list from list
# print(data[2:]) #start from index 2 and print at end
# print(data[:5]) # start from 0 index and end required

# cange list items
# data[2] = "Ahmad"
# print(data)

#  List Methods
# Python provides many useful methods for working with lists.

# Method	Description
# append(x)	Adds x to the end of the list
# insert(i, x)	Inserts x at index i
# remove(x)	Removes the first occurrence of x
# pop(i)	Removes the item at index i (or last if i is not provided)
# sort()	Sorts the list in ascending order
# reverse()	Reverses the list
# count(x)	Counts occurrences of x
# index(x)	Returns the index of x


# list comprehension

count = [i for i in range(1,9)]
print(count)

# task
# sum of elements

# num = [1,2,1,3,4,5]
# print(sum(num))

# second method

# total = 0
# for i in num:
#     total = total+i
# print(f"sum of elements {total}")

# task 2
# Write a Python program that removes duplicates from a list.

num = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5]
uniques_num = []
for i in num:
    if i not in uniques_num:
        uniques_num.append(i)
print(uniques_num)

# 2nd method 

unique = list(dict.fromkeys(num))
print(unique)
# 3rd method
unique1= list(set(num))
print(unique1)
