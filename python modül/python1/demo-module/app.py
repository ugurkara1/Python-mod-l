"""
    module1(db)         :urunler
    module2(methods)    :urunEkle(),urunGuncelle(),urunleriGetir()
    module2(app)        :

        yeni ürün ekleme=>urunEkle("ıphone 11 pro",7000)
        urun güncelle   =>urunGuncelle(1,"ıphone 12 pro",8000)
        urunleri listele =>urunleriGetir()
"""
 
 
from methods import *
urunleriGetir()
urunEkle("iphone 11 pro",8000)
urunleriGetir()


