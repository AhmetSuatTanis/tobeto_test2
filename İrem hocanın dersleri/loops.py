for i in range(10):
    print(i)

#start: döngü kaç sayısından başlasın (default 0)
#stop: döngü kaç kere tekrar etsin
#step: döngü kaç kaç arttırılsın (default 1 er 1 er)

#ilki kaçtan başladığı, ikinci kaça kadar gideceği ama dahil değil, üçüncü kaçar kaçar artacağı yönünde    
# for i in range(1,11,1):
#     print(i)

#kullanıcının vereceği üst limit ile alt limitten bu üst limite kadar olan tüm çift sayıları ekrana yazdıralım

print("kullanıcının vereceği üst limit ile alt limitten bu üst limite kadar olan tüm çift sayıları ekrana yazdıralım")
sayi1=int(input("Bir üst limit sayısı giriniz: "))
sayi2=int(input("Bir alt limit sayısı giriniz: "))
print("girdiğiniz sayılar arasındaki çift sayılar bu şekildedir")
for i in range(sayi2,sayi1+1):
    if i%2==0:
        print(i)

#kullanıcının girdiği sayılar arasındaki en büyüğünü bulan bir program
biggestValue=0
for i in range(5):
    sayi=int(input(f"{i+1}. sayıyı giriniz: "))
    if sayi > biggestValue:
        biggestValue=sayi

print(f"Girdiğiniz sayılar arasında en büyük olanı: {biggestValue}")
print("Girdiğiniz sayılar arasında en büyük olanı:",biggestValue)

sayilar=[]
for i in range(5):
    sayilar.append(int(input(f"{i+1}. sayıyı giriniz: ")))
    sayilar.sort(reverse=True)  #descending sıralama oldu

print(f"Girdiğiniz sayılar arasında en büyük olanı: {sayilar[0]}")


sayilar=[]
for i in range(5):
    sayilar.append(int(input(f"{i+1}. sayıyı giriniz: ")))
    
print(min(sayilar))
print(f"Girdiğiniz sayılar arasında en büyük olanı: {min(sayilar)}")
print(max(sayilar))
print(f"Girdiğiniz sayılar arasında en büyük olanı: {max(sayilar)}")


students = ["Ahmet","Tuba","Abdullah","Onur","Dilara"]
#length = uzunluk
print(len(students))

for i in range(len(students)):
    print(f"{i+1}. Öğrenci: {students[i]}")

x=1
for i in students:
    print(f"{x}. Öğrenci: {i}")
    x+=1

#break: ilgili döngüyü o anda kırar ve dışına çıkar
for i in range(len(students)):
    if i > 3:
        break
    print(f"{i+1}. Öğrenci: {students[i]}")

#continue: iterasyondaki current değeri atla ve bir sonraki değer ile devam et
for i in students:
    if i=="Tuba":
        continue
    print(f"{x}. Öğrenci: {i}")

# while döngüsü

i=0
while i<10:
    print("Merhaba")
    i= i+2

    


    
    