from muzisyen import muzisyen

from yanflüt import yanflut

from keman import keman

yanflut = yanflut()
yanflut.Markası = "yamaha"
yanflut.Aciklama = "pahalı"
sound = yanflut.Cal()

muzisyen = muzisyen()
muzisyen.adi = "beste"
muzisyen.soyadi = "karademir"
muzisyen.Enstruman = yanflut

result = """
adı = : {}
soyadı : {}
Enstruman sesi : {} 
marka : {}
açıklama : {}
""".format(muzisyen.adi,
           muzisyen.soyadi,
           sound,
           muzisyen.Enstruman.Markası,
           muzisyen.Enstruman.Aciklama)
print(result)