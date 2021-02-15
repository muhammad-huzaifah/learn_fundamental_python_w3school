# module

import mymodule

mymodule.greeting("Ujeb")

# variables in module
import mymodule

a = mymodule.person1["age"]
print(a)

# naming a module
import mymodule as mx

a = mx.person1["age"]
print(a)

# built in module
import platform

x = platform.system()
print(x)

# using dir() function
import platform

x = dir(platform)
print(x)

# import from module
from mymodule import person1

print(person1["age"])
