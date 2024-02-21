class Student:
    def __init__(self, isim, soyisim,bolum):
        self.isim= isim
        self.soyisim= soyisim
        self.bolum=bolum
        
    
    def bilgi(self):
        print(f"öğrenci adı soyadı: {self.isim} {self.soyisim}  -->Bölümü: {self.bolum}")
    
    
    def ortalamaHesaplama(self, vize, final):
        adSoyad=self.isim+" "+self.soyisim
        ortalama= (vize*0.4) + (final*0.6)
        print(f"{adSoyad} ortalaması: {ortalama}")

# student1= Student("Ayşe", "Yılmaz")
# student2= Student("Ali", "Kaya")
# student3= Student("Ahmet", "Ayaz")
# student4= Student("Merve", "Öztürk")
# student1.bilgi()
# student1.ortalamaHesaplama(70, 80)
# student2.bilgi()
# student2.ortalamaHesaplama(50, 75)
# student3.bilgi()
# student3.ortalamaHesaplama(60, 80)
# student4.bilgi()
# student4.ortalamaHesaplama(75, 90)

