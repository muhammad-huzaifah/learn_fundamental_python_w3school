thisdict = {
    "barang": "ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

thisdict = {
    "barang": "ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020

}
print(thisdict)

thisdict = {
    "barang": "ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)

thisdict = {
    "barang": "ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))

thisdict = {
    "barang": "ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)

thisdict = {
    "barang": "ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.get("model")
print(x)

thisdict = {
    "barang": "ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.keys()
print(x)

# car = {
#     "barang": "ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x = car.keys()
# print(x)
#
# car["color"] = "white"
# print(x)

car = {
    "barang": "ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.values()
print(x)

car = {
    "barang": "ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x)
car["year"] = 2020
print(x)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.items()
print(x)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)
car["year"] = 2020
print(x)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict = {"brand": "Ford", "model": "Mustang", "year": 2018}
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year":2020})
print(thisdict)

#remove
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# del thisdict
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

# Loop

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(thisdict[x])

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict.keys():
    print(x)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x, y in thisdict.items():
    print(x, y)

# copy

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#nested dictionaries

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)

#excercise

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))