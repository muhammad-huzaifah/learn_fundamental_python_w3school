if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two!")

x = 5
y = "Hello, World"

# This is a comment.
print("\nHello, World")

print("\nHello, World!")  # This is a comment

# print("Hello, World!")
print("\nCheers, Mate!")

# This is a comment
# Written in
# more than just one line
print("\nHello, World!")

"""
This is a comment
written in 
more than just one line
"""

print("\nHello, World!")

x = 5
y = "John"
print(x)
print(y)

x = 4  # x is of type int
x = "\nSally"  # x is now of type str
print(x)

x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'
print(x)

a = 4
A = "Sally"
print(a)
print(A)

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(myvar)
print(my_var)
print(_my_var)
print(MYVAR)
print(myvar2)
print(myVar)

x, y, z = "orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "awesome"
print("Python is " + x)

x = "\nPython is "
y = "awesome "
z = x + y
print(z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
# print(x + y)

x = "awesome"


def myfunc():
    print("\nPython is " + x)


myfunc()

x = "awesome"


def myfunc():
    x = "fantastic"
    print("\nPython is " + x)


myfunc()

print("Python is " + x)


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("\nPython is " + x)

x = 5
print(type(x))

x = "Hello World"
print(x)
print(type(x))

x = 20
print(x)
print(type(x))

x = 20.5
print(x)
print(type(x))

x = 1j
print(x)
print(type(x))

x = ["apple", "banana", "cherry"]
print(x)
print(type(x))

x = ("apple", "banana", "cherry")
print(x)
print(type(x))

x = range(6)
print(x)
print(type(x))

x = {"name": "John", "age": 36}
print(x)
print(type(x))

x = {"apple", "banana", "cherry"}
print(x)
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

x = True
print(x)
print(type(x))

x = b"Hello"
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))

x = str("Hello World")
print(x)
print(type(x))

x = int(20)
print(x)
print(type(x))

x = float(20.5)
print(x)
print(type(x))

x = complex(1j)
print(x)
print(type(x))

x = list(("apple", "banana", "cherry"))
print(x)
print(type(x))

x = tuple(("apple", "banana", "cherry"))
print(x)
print(type(x))

x = range(6)
print(x)
print(type(x))

x = dict(name="John", age=36)
print(x)
print(type(x))

x = set(("apple", "banana", "cherry"))
print(x)
print(type(x))

x = frozenset(("apple", "banana", "cherry"))
print(x)
print(type(x))

x = bool(5)
print(x)
print(type(x))

x = bytes(5)
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))

x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = - 3255522

print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

x = 3 + 5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(x))
print(type(y))
print(type(z))

import random

print(random.randrange(1, 10))

# casting

x = int(1)
y = int(2.8)
z = int("3")

print(x)
print(y)
print(z)

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")

print(x)
print(y)
print(z)
print(w)

x = str("s1")
y = str(2)
z = str(3.0)

print(x)
print(y)
print(z)

print("Hello")
print('Hello')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua"""
print(a)

a = '''Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua'''
print(a)

a = "Hello, World!"
print(a[0])

for x in "banana":
    print(x)

a = "Hello, World"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "Free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(","))

a = "Hello"
b = " World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# age = 36
# txt = "My name is John, I am " + age
# print(txt)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollar for {0} piece of  item {1}."
print(myorder.format(quantity, itemno, price))

# txt = "We are the so-called "Vikings" from the north"
# print(txt)

txt = "We are the so-called \"vikings\" from the north."
print(txt)

txt = 'It\'s alright.'
print(txt)

txt = "This will insert one \\ (backslash)."
print(txt)

# txt = "Hello\nWorld!"
# print(txt)

txt = "Hello\rWorld!"
print(txt)

txt = "Hello\tWorld!"
print(txt)

txt = "Hello \bWorld!"
print(txt)

txt = "\110\145\154\154\157"
print(txt)

txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)

txt = "36 is my age."
x = txt.capitalize()
print(x)

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))


# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool())
# print(bool([]))
# print(bool({}))


class MyClass():
    def __len__(self):
        return 0


myobj = MyClass()
print(bool(myobj))


def myFunction():
    return True


print(myFunction())


def myFunction():
    return True


if myFunction():
    print("YES!")
else:
    print("NO!")

x = 200
print(isinstance(x, int))

print(10 + 5)

x = 5
y = 3

print(x + y)

x = 5
y = 3

print(x - y)

x = 5
y = 3

print(x * y)

x = 12
y = 3

print(x / y)

x = 5
y = 2

print(x % y)

x = 2
y = 5

print(x ** y)

x = 15
y = 2

print(x // y)

x = 5
print(x)

x = 5
x += 3
print(x)

x = 5
x -= 3
print(x)

x = 5
x *= 3
print(x)

x = 5
x /= 3
print(x)

x = 5
x %= 3
print(x)

x = 5
x //= 3
print(x)

x = 5
x **= 3
print(x)

x = 5
x &= 3
print(x)

x = 5
x |= 3
print(x)

x = 5
x ^= 3
print(x)

x = 5
x >>= 5
print(x)

x = 5
x <<= 3
print(x)

x = 5
y = 3
print(x == y)

x = 5
y = 3
print(x != y)

x = 5
y = 3
print(x > y)

x = 5
y = 3
print(x < y)

x = 5
y = 3
print(x >= y)

x = 5
y = 3
print(x <= y)

x = 5
print(x > 3 and x < 10)

x = 5
print(x > 3 or x < 4)

x = 5
print(not(3 < x < 10))

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]