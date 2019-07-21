
from abc import ABCMeta, abstractmethod

class BasePhone(metaclass = ABCMeta):
    __metaclass__ = ABCMeta

    def __init__(self,marka, model, fiyat):
        self.Marka = marka
        self.Model = model
        self.Fiyat = fiyat

    def sound(self):
        return "çan sesi"

class samsung(BasePhone):
    def __init__(self,marka, model, fiyat, tedarikci):
        super(samsung, self).__init__(marka,model,fiyat)
        self.Tedarikci = tedarikci

    def Sound(self):
        return "samsung default mobil phone sound"

class apple(BasePhone):
    def __init__(self,marka, model, fiyat, garanti):
        super(apple, self).__init__(marka,model,fiyat)
        self.Garanti = garanti

    def Sound(self):
        return "apple default mobil phone sound"


Apple = apple("apple","8splus",10000,"TR")
print("""
marka        : {}
model        : {}
fiyat        : {}
garanti      : {}
telefon sesi : {}
""".format(Apple.Marka, Apple.Model, Apple.Fiyat, Apple.Garanti, Apple.Sound()))

Samsung = samsung("samsung", "S10plus", 10000, "KVK")
print("""
marka        : {}
model        : {}
fiyat        : {}
tedarikci    : {}
telefon sesi : {}
""".format(Samsung.Marka, Samsung.Model, Samsung.Fiyat, Samsung.Tedarikci, Samsung.Sound()))
