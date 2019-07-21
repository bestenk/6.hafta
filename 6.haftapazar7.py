from enum import Enum, unique, auto
@unique # sınıf içerisinde aynı index değerine sahip enum oluşturmaya izin vermez



class icecek (Enum):
    vanilya  = auto()
    cikolata = auto()
    visne    = 7
    muzlu    = auto()
    cilek    = 35
    kahveli  = auto()

liste = list(icecek)
print(liste)