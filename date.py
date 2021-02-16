# dates
import datetime

x = datetime.datetime.now()

print(x)

# date output
print(x.year)
print(x.strftime("%A"))


# Create Date Objects
x = datetime.datetime(2020, 5, 17)

print(x)

# strftime() methode
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))