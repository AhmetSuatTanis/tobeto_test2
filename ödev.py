#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
print("Vücut kitle indeksinizi bulan program")
print()
boy = float(input("Boyunuzu giriniz(örn: 1.80) :"))
kilo = int(input("Kilonuzu giriniz (örn: 75) :"))
endeks = float(kilo /(boy*boy))
formatliEndeks=f"{endeks:.2f}"
vucutIndeksi=f"Vücut kitle indeksiniz: {formatliEndeks} olarak hesaplanmıştır"
print(vucutIndeksi)

#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
print("Maaş ve zam oranını girerek yeni maaşınızı hesaplayan program")
print()
maas = int(input("Maaşınızı giriniz: "))
zamOrani=float(input("Zam oranını tam sayı olarak giriniz: "))
zamliMaas= float(maas+maas*(zamOrani/100))
print("Zamlı  maaşınız: ",zamliMaas," TL")

#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
print("Girilen 3 sayıdan en büyüğünü bulan program")
print()
birinciTamsayi=int(input("birinci sayıyı giriniz: "))
ikinciTamsayi=int(input("ikinci sayıyı giriniz: "))
ucuncuTamsayi=int(input("üçüncü sayıyı giriniz: "))
enBuyukSayi=max(birinciTamsayi,ikinciTamsayi,ucuncuTamsayi)
print("Girilen en büyük sayı: ",enBuyukSayi)
  
#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
print("Dairenin alanı ve çevresini heseplayan program")
print()
yariCap=float(input("Dairenin yarı çapını giriniz (cm) : "))
pi=3.14
daireAlani=pi*yariCap*yariCap
daireCevre=f"{(2*pi*yariCap):.2f}"
print("Dairenin Alanı =",daireAlani, " cm  karedir")
print("Dairenin Çevresi=",daireCevre, " cm dir")

#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
print("Girilen tam sayının panlindrom olup olmadığını bulan program")
print()
sayi=(input("lütfen bir tam sayı giriniz:"))

tersten = "" 
for rakam in sayi:
    tersten = rakam + tersten
    
print ()   
if tersten==sayi:
    print(sayi,"Sayısı Palindrom bir sayıdır")
else:
    print(sayi,"Sayısı Palindrom bir sayı değildir")    



