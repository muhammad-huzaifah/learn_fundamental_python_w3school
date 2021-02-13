# class

class MyClass:
    x = 5


print(MyClass)


# object

class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


# function __init__()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# Methode object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()


# self parameter

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("ujeb", 42)
p1.myfunc()


# modify object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("ujeb", 42)
p1.age = 43
print(p1.age)


# delete object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("ujeb", 42)
del p1.age


# print(p1.age)

class Person:
    pass


# Exercise

class MyClass:
    x = 5


print(MyClass)
