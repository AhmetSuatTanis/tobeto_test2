# 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

print("20 elemanlı Fibonacci serisini yazan program")

geciciSayi=0
ilkSayi=1  
ikinciSayi=1  
listOfFibonacci=[]
listOfFibonacci.append(ilkSayi)
listOfFibonacci.append(ikinciSayi)

for i in range(18): 
    geciciSayi=ilkSayi+ikinciSayi  
    listOfFibonacci.append(geciciSayi) 
    ilkSayi=ikinciSayi  
    ikinciSayi=geciciSayi  

print(listOfFibonacci)


# 2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

print("Girilen sayının mükemmel sayı olup olmadığını bulan program")

sayi=int(input("Lütfen bir tam sayı giriniz :"))
toplam=0
i=1
while i<=sayi/2:
    if sayi%i==0:
        toplam+=i
        i+=1
    else:
        i+=1
if toplam==sayi:
    print(f"Girilen {sayi} sayısı mükemmmel sayıdır")
else:
    print(f"Girilen {sayi} sayısı mükemmmel sayı değildir") 


# 3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

print("Lütfen iki adet tam sayı giriniz")
sayi1=int(input("Birinci sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))

kucukSayi=0
if sayi1>sayi2:
    kucukSayi=sayi2
else:
    kucukSayi=sayi1

ebob=1
i=2
while i<=kucukSayi:
    if sayi1%i==0 and sayi2%i==0:
        ebob=i
        i+=1
    else:
        i+=1

ekok= (sayi1*sayi2)//ebob

print(f"{sayi1} ve {sayi2} sayılarının en büyük ortak böleni: {ebob}")
print(f"{sayi1} ve {sayi2} sayılarının en küçük ortak katı: {ekok}")

# 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

sayi=int(input("Lütfen bir tam sayı giriniz: "))
i=2
while i<sayi:
    if sayi%i==0:
        print(f"{sayi} sayısı asal değildir")
        break
    else:
        i+=1
        if i==sayi:
            print(f"{sayi} sayısı asaldır")

                
# 5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 
            
print("Girilen sayının asal çarpanlarını bulan program")
sayi=int(input("Bir sayı giriniz: "))
tempSayi=sayi
i = 2
dizi=[]
while i <= tempSayi/2:
    if tempSayi % i == 0:
        dizi.append(i)
        tempSayi //= i
    else:
        i += 1
if len(dizi)>=1:
 print(sayi, f"sayısının asal çarpanları: {dizi}")
else:
   print(sayi,"Sayısının asal çarpanı yoktur. çünkü kendisi bir asal sayıdır")
    


