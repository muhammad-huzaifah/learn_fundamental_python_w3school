# function

def my_function():
    print("Hello from a function")


my_function()


# Arguments
def my_function(fname):
    print(fname + "Refsnes")


my_function("Emil ")
my_function("Tobias ")
my_function("Linus ")


def my_function(fname, lname):
    print(fname + "" + lname)


my_function("Emil ", "Refsnes")


def my_function(fname, lname):
    print(fname + "" + lname)


# my_function("Emil")

# args

def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# keyword arguments (kwargs)

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# keyword arguments **kwargs

def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


# Default Parameter Value

def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# passing a list as an Argument
def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_function(fruits)


# return values

def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


# pass statement
def myfunction():
    pass


# recursion
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\nRecursion Example Results")
tri_recursion(6)


# exercise
def my_function():
    print("Halo dari suatu fungsi")


my_function()
