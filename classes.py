#nesne, obje, sınıf
class Human:
    #properties, attributes, => özellik nitelik
    #init içinde olan parametlerin class içinde önceden tanımlanmasına gerek yoktur.
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        print("yapıcı blok çalıştı")

    def age1(self):
         print(self.age)
    
    def talk(self,message):
        print(message)
    
    def walk(self):
        print(f"{self.name} is walking...")

human1= Human("Ahmet",32)  #instance (örnek) oluşturduk
human1.talk("Hocam")
human1.walk()
human1.age1()

#classların içinde bir fonksiyon tanımlıyorsak
#ilk parametresi rezervedir => self parameter

    





