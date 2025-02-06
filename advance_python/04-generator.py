# A generator is a special type of iterator that uses the yield keyword to return values one at a
# time, lazily. This makes it memory-efficient for large data.


def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1

# Using the generator
for num in count_up_to(5):
    print(num)
