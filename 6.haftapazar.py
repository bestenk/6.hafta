# decorater

class personel :
    def __init__(self,isim, soyisim):
        self.firstname = isim
        self.lastname  = soyisim

    @property
    def email(self):
        return "{}.{}".format(str(self.firstname).lower(), str(self.lastname).lower())

    @property # isim soyisim alanında property olarak belirliyoruz
    def isim_soyisim(self):
        return "{} {}".format(self.firstname,self.lastname)

    @isim_soyisim.setter
    def isim_soyisim(self,parametre):
        ad,soyad       = parametre.split(' ')
        self.firstname = ad
        self.lastname  = soyad


    @isim_soyisim.deleter
    def isim_soyisim(self):
        print("kişi silindi")
        self.firstname = None
        self.lastname  = None

per1 = personel("beste","karademir")
print(per1.firstname)
print(per1.lastname)
print(per1.email)

per1.isim_soyisim = "simge karademir"
print(per1.firstname)
print(per1.lastname)
print(per1.email)
