class Student:
    def __init__(self, isim, soyisim,vize,final,bolum):
        self.isim= isim
        self.soyisim= soyisim
        self.vize=vize
        self.final=final
        self.bolum=bolum
    
    def bilgi(self):
        print(f"öğrenci adı soyadı: {self.isim} {self.soyisim} -->Bölümü: {self.bolum}")
    
    def ortalamaHesaplama(self):
        ortalama= (self.vize*0.4) + (self.final*0.6)
        return ortalama
    
    





