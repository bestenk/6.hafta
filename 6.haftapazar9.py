# flag kullanımı oluşturduğunuz enum dğerlerinin sayısal karşılığının benzersi ve birden fazla enum değerinin bir enum değerine karışılık glememsi



from enum import Flag, auto, Enum

class renkler (Enum):
    kırmızı = auto() # enum 1 flag 1
    sarı = auto()    # enum 2 flag 2
    mavi = auto()    # enum 3 flag 4
    turuncu = auto() # enum 4 flag 8
    yeşil = auto()   # enum 5 flag 16
    pembe = auto()   # enum 6 flag 32
    beyaz = kırmızı | mavi| sarı # 7

print(repr(renkler.kırmızı and renkler.mavi))
liste = list(renkler)
print(liste)

print((renkler.sarı and renkler.pembe).value)

