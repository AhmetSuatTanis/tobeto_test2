#) Kullanıcın girdiği 5 basamaklı bir sayının, 
#basamaklarının toplamını ekrana yazdıran python kodlarını yazınız?
# toplam=0
# sayi=int(input("5 basamaklı bir sayı giriniz"))
# for rakam in sayi:
#     toplam+=rakam+toplam
# print(toplam)

#GİRİLEN SAYISIN ASAL ÇARPANLARINI BULAN PROGRAM
# print("Girilen sayının asal çarpanlarını bulan program")
# sayi=int(input("Bir sayı giriniz: "))
# tempSayi=sayi
# i = 2
# dizi=[]
# while i <= tempSayi/2:
#     if tempSayi % i == 0:
#         dizi.append(i)
#         tempSayi //= i
#     else:
#         i += 1
# if len(dizi)>=1:
#  print(sayi, f"sayısının asal çarpanları: {dizi}")
# else:
#    print(sayi,"Sayısının asal çarpanı yoktur. çünkü kendisi bir asal sayıdır")

#FİBONACCİ SERİSİNİ YAZDIRAN PROGRAM
# #1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233
# geciciSayi=0
# ilkSayi=1  #1 1 2 3
# ikinciSayi=1  #1 2 3 5
# listOfFibonacci=[1,1]
# for i in range(18): #zaten elimizde 2 tanesi mevcut 1, 1 geri kalan 18 adet için döngü yaptık.
#     geciciSayi=ilkSayi+ikinciSayi  #2 3 5 8
#     listOfFibonacci.append(geciciSayi) 
#     ilkSayi=ikinciSayi  #1 2 3 5
#     ikinciSayi=geciciSayi  #2 3 5 8

# print(listOfFibonacci)

# 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

# sayi=int(input("Lütfen bir tam sayı giriniz: "))
# i=2
# while i<sayi:
#     if sayi%i==0:
#         print(f"{sayi} sayısı asal değildir")
#         break
#     else:
#         i+=1
#         if i==sayi:
#             print(f"{sayi} sayısı asaldır")

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
