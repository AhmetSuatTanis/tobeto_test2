ortalamaNot= int(input("Lütfen ortalamanızı giriniz: "))

#print(type(ortalamaNot))

if ortalamaNot > 50:
    print("Başarılı")
    if ortalamaNot >80:
        print("Bravo!!!")
#else if
elif ortalamaNot >40:
    print("Ortalama")        
else:
    print("Dersten kaldınız")

print("if bloğundan bağımsız bir kısımdayım")


if ortalamaNot > 85 and ortalamaNot<100:
    print("Başarılı")
elif ortalamaNot >70 and ortalamaNot<85:
    print("Ortalama")        
else:
    print("Dersten kaldınız")

