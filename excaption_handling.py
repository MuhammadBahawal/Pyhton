# task 1
# num1 = int(input("enter the first number: "))
# num2 = int(input("enter the second number: "))

# try:
#     result = num1/num2
#     print(result)
# except Exception as e :
#     print(f"error: {e}")
    
# task 2

# try:
#     num = int(input("enter the number: "))
#     print(f"you enter {num}")
# except ValueError:
#     print(ValueError)

# task 3 
try:
    file = open("hello.txt","r")
    data = file.write("Excaption handling task")
    print(data)
except Exception as e:
    print(e)
finally:
    print("program Endedp0ok")
