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



