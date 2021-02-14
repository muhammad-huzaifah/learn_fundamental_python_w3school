# local scope
def myfunc():
    x = 300
    print(x)


myfunc()


# function inside function
def myfunc():
    x = 300

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunc()

# global scope
x = 300


def myfunc():
    print(x)


myfunc()

print(x)

# naming variabel
x = 300


def myfunc():
    x = 200
    print(x)


myfunc()

print(x)


# global keyword
def myfunc():
    global x
    x = 400


myfunc()

print(x)

x = 300


def myfunc():
    global x
    x = 200


myfunc()

print(x)
