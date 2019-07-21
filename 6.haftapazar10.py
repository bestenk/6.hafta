from enum import Enum

class renkenum(Enum):
    kırmızı = 1
    sarı = 2
    mavi = "blue"
    mail = "mail adresi, @ işareti içermelidir.kontrol et"

print(repr(renkenum.mavi)) #<renkenum.mavi : 'blue'>
print(renkenum.mail.value)

class intenum(int, Enum): # birinci parametrede verilen veri tipi ne ise içeride tanımladığınız vlue değeride o yipte olmak zorundadır
    kırmızı = 1
    sarı = 2

print(intenum.kırmızı )

class floatenum(float, Enum):
    kırmızı = 1
    sarı = 2
    yeşil = 1.10

print(floatenum.yeşil.value)