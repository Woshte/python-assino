f = open('assignment.txt', 'r')
print(f.readline(), end="")
print(f.readline())
print(f.readline())



write = open("write", "w")
write.write("Python to the world, I suppose")


write = open("write", "a")
write.write(" This is Awesome") 

 #with finally
try:
    file = open("sample.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found.May be you have not created it yet")
finally:
    file.close()