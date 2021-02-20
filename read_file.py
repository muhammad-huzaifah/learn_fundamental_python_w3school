f = open("demofile.txt", "r")
print(f.read())

f = open("c:\\myfiles\welcome.txt", "r")
print(f.read())

# read only parts of the file
f = open("demofile.txt", "r")
print(f.read(5))

# read lines
f = open("demofile.txt", "r")
print(f.readline())

# 2 read lines
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

f = open("demofile.txt", "r")
for x in f:
    print(x)

# close file
f = open("demofile.txt", "r")
print(f.readline())
f.close()