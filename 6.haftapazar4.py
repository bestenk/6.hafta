# enum : değişmeyen sabit değerler

from enum import Enum

class color(Enum):
    red = 1
    green = 2
    blue = 3


print(color.blue)

print(repr(color.green))

print(type(color.red))

print(isinstance(color.red,color)) #true
print(color.red.name)