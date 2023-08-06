import db

def urunEkle(urunAdi,fiyat):
    db.urunler.append({
        "id": len(db.urunler)+1,
        "UrunAdi":urunAdi,
        "fiyat":fiyat
    })

def urunGuncelle(id,urunAdi,fiyat):
    for urun in db.urunler:
        if(urun["id"]==id):
            urun["UrunAdi"]=urunAdi
            urun["fiyat"]=fiyat
            break

def urunleriGetir():
    for urun in db.urunler:
        print(f"id {urun['id']} ürün adi :{urun['urunAdi']} fiyat:{urun['fiyat']}")
