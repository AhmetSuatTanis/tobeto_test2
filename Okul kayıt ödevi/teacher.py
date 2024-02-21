class Teacher:

    def __init__(self, isim, soyisim, bolum):
        self.isim= isim
        self.soyisim= soyisim
        self.bolum= bolum
    
    def bilgi(self):
        print(f"öğretmen adı soyadı: {self.isim} {self.soyisim}  --> Bölümü: {self.bolum}")

    def zamliMaas(self, maas, zamOrani):
        zamliMaas= maas + (maas* zamOrani/100)
        print(f"{self.isim} {self.soyisim} zamlı maaşınız: {zamliMaas} TL")

# teacher1= Teacher("Nesibe", "Kaya", "Matematik")
# teacher2= Teacher("Ahmet", "Tanış", "Fizik")
# teacher3= Teacher("Özlem", "Akman", "Edebiyat")
# teacher4= Teacher("Kevser","Yılmaz","Kimya")
# teacher1.bilgi()
# teacher1.zamliMaas(1000, 50)
# teacher2.bilgi()
# teacher2.zamliMaas(2000, 50)
# teacher3.bilgi()
# teacher3.zamliMaas(3000, 50)
# teacher4.bilgi()
# teacher4.zamliMaas(4000, 50)
