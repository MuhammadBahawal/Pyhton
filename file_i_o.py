
f = open("d:/smit/Pyhton/filei/file.txt", "r")
data = f.read()
print(data)
f.close()

write = "hello adeel how are you "
B = open('file.txt','w')
insrt = B.write(write)
print(insrt)

lines = f.readlines()
print(lines)

line1 = f.readline()
print(line1)