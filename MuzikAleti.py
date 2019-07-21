from abc import ABCMeta, abstractmethod

class MuzikAleti(metaclass = ABCMeta):
    Marka = ""
    Aciklama = ""

    @abstractmethod
    def Cal(self):
        pass

    def Akort(self):
        return "cihaz Akort Edildi"