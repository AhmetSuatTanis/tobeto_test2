sayilar = [100,200,300,"Merhaba",True,15.5]
#indis 0 dan başlar
print(sayilar[1])
print(sayilar)

sayilar.append(400)
print(sayilar)
sayilar.remove("Merhaba") #değere göre işlem yapar ve siler # ilk yakaladığını siler
print(sayilar)

sayilar.pop()  #indexe göre siler (default son index)
print(sayilar)

sayilar.pop(2)  #indexe göre siler

add = [700,800,900]
sayilar.extend(add)
print(sayilar)

sayilar.clear()  #listenin içini boşaltıyoruz
print(sayilar)
