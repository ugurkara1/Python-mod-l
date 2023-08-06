import module

sonuc=module.sayi
sonuc=module.sayilar

sonuc=module.ogrenci
sonuc=module.ogrenci["ad"]
sonuc=module.ogrenci["notlar"]

print(sonuc)
import module as m
sonuc=m.sayilar
from module import ogrenci,topla
sonuc=ogrenci
sonuc=topla(10,20)
print(sonuc)

from module import *

sonuc=sayi
print(sonuc)