# Uses threads (lightweight processes) to run multiple tasks concurrently.
# the main purpose of this to run multiple tasks and multiple functions at same time 
# python have default one thread which is main we 
#thread is a pre defined class which is in thread module

# threads are independent

#single threading 

from threading import Thread
from time import sleep

class Teacher(Thread):
    def run(self):  
        print("Hello Teacher")
        sleep(2)

class Student(Thread):
    def run(self):
        print("Hello Student")
        sleep(2)

obj1 = Teacher()
obj2 = Student()

# Start the threads first
obj1.start()
obj2.start()

# Now join to ensure both threads complete
obj1.join()
obj2.join()

print("done")
