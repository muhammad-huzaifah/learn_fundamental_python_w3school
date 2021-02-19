# exception handling
"""
try:
    print(x)
except:
    print("An exception occured")
"""

# Many Exception
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# else

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Finally
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

try:
    f = open("demofile.txt")
    f.write("Lorem Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

# raise an exception
"""
x = -1
if x < 0:
    raise Exception("Sory, no numbers below zero")
print(x)
"""

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
print(x)