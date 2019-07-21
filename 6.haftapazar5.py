from enum import Enum

class icecek (Enum):
    vanilya = 7
    cikolata = 4
    visne = 3
    muzlu = 1


for x in icecek:
    print(x)

for ad, uye in icecek.__members__.items():
    print(str(ad) + " " + str(uye))
    print(str(ad) , str(uye))
    print(ad , uye)