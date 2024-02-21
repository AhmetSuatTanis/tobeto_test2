# ---Bir okul kayıt sistemi kodlayalım---
# Öğrenci ve Öğretmen classlarını farklı dosyalarda oluşturalım. 
# Bu classlar içerisinde en az 2 property 2 method barındırmalıdır.
# Daha sonra bir dosyada öğrenci ve öğretmen classlarını import ederek 
# bir listede kayıtlı öğrenci/öğretmen bilgilerini ayrı ayrı tutalım. 
# Listeye ekleme yapan, listedeki tüm elemanları ekrana yazan fonksiyonları geliştirelim ve konsolda test edelim.

from student import Student
from teacher import Teacher

ogrenciListesi=[]
ogretmenListesi=[]

def addStudent(isim,soyisim,vize,final,bolum):
    
    newStudent=Student(isim,soyisim,vize,final,bolum)
    ogrenciListesi.append(newStudent)
    
    
def printStudent():
    print("Ögrenci Listesi:")
    print()
    for student in ogrenciListesi:
        student.bilgi()
        print(f"ortalama notu",int(student.ortalamaHesaplama()))

def addTeacher(isim,soyisim,bolum,maas,zamOrani):

    newTeacher=Teacher(isim,soyisim,bolum,maas,zamOrani)
    ogretmenListesi.append(newTeacher)

def printTeacher():
    print()
    print("Öğretmen Listesi:")
    print()
    for teacher in ogretmenListesi:
        teacher.bilgi()
        eskiMaas=teacher.maas
        print(f"Eski maaş=",eskiMaas, "TL")
        print(f"zamli maas=", int(teacher.zamliMaas()),"TL")


addStudent("Nesibe","Kaya",70,90,"Sayısal")
addStudent("Ahmet","Tanış",50,70,"Sözel")
addStudent("Mehmet","Kurt",65,75,"Eşit ağırlık")
addStudent("Ali","Öztürk",60,85,"Sayısal")
addStudent("Merve","Yılmaz",50,90,"Eşit Ağırlık")

addTeacher("Özlem","Akman","Matematik",20000,30)
addTeacher("Emir","Yılmaz","Fizik",15000,20)
addTeacher("Reyhan","Akman","Kimya",20000,30)
addTeacher("Nihat","Nurdağ","Edebiyat",15000,30)
addTeacher("Kevser","Yılmaz","Türkçe",17000,30)

printStudent()
printTeacher()


