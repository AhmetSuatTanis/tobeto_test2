# ---Bir okul kayıt sistemi kodlayalım---
# Öğrenci ve Öğretmen classlarını farklı dosyalarda oluşturalım. 
# Bu classlar içerisinde en az 2 property 2 method barındırmalıdır.
# Daha sonra bir dosyada öğrenci ve öğretmen classlarını import ederek 
# bir listede kayıtlı öğrenci/öğretmen bilgilerini ayrı ayrı tutalım. 
# Listeye ekleme yapan, listedeki tüm elemanları ekrana yazan fonksiyonları geliştirelim ve konsolda test edelim.

from student import Student
from teacher import Teacher

ogrenciListesi= []
ogretmenListesi= []

def ogrenciEkle(*args):
    for student in args:
        ogrenciListesi.append(student)

def ogretmenEkle(*args):
    for teacher in args:
        ogretmenListesi.append(teacher)

def tumOgrencileriGoster():
    print("Tüm öğrencilerin listesi:")
    print()
    for ogrenci in ogrenciListesi:
        ogrenci.bilgi()

def tumOgretmenleriGoster():
    print("Tüm öğretmenlerin listesi:")
    print()
    for ogretmen in ogretmenListesi:
        ogretmen.bilgi()


student1=Student("Ayşe", "Yılmaz","Sayısal")
student2=Student("Mevlüt", "Kar","Sözel")
student3=Student("Turan", "Yakın","Eşit ağırlık")
student4=Student("Azize", "Dönmez","Sayısal")

teacher1= Teacher("Nesibe", "Kaya", "Matematik")
teacher2= Teacher("Ahmet", "Tanış", "Fizik")
teacher3= Teacher("Özlem", "Akman", "Edebiyat")
teacher4= Teacher("Kevser", "Yılmaz", "Kimya")

ogrenciEkle(student1,student2,student3,student4)
# ogrenciEkle(student1)
# ogrenciEkle(student2)
# ogrenciEkle(student3)
# ogrenciEkle(student4)

ogretmenEkle(teacher1,teacher2,teacher3,teacher4)
# ogretmenEkle(teacher1)
# ogretmenEkle(teacher2)
# ogretmenEkle(teacher3)
# ogretmenEkle(teacher4)

tumOgrencileriGoster()
print()
tumOgretmenleriGoster()
