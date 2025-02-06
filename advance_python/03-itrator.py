# An iterator is an object that implements two methods:
# __iter__() → Returns the iterator object itself.
# __next__() → Returns the next value in the sequence.


class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  
        self.current += 1
        return self.current - 1

# Using the iterator
iterator = MyIterator(0, 5)
for num in iterator:
    print(num)
