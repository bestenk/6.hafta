# abstract


from abc import ABCMeta, abstractmethod

class baseclass(Metaclass = ABCMeta):
   # __metaclass__ = ABCMeta

   def printHam(self):
       return "default sesi"


class personel(baseclass):
    def printHam(self):
        return "personel sesi"


per         = personel()
print(per.printHam())