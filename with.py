# similar to open file but in this we not restrict to close the file
hello = "hello how are you "
with open("file.txt", "a") as f:
    data = f.write(hello)
print(data)