print("Merhaba Tobeto Test Ekibi")

#değişkenler
#metinsel-numerik-obje

text = "Hello"
kullaniciAdi="irem"
print(text)

studentCount = "45" #string 
print(studentCount+"5")  #455 olur string olarak ekler yanına

studentCount1 = 5  #integer=>tamsayı
print(studentCount1+5)   

averagePoint = 25.5  # double - decimal- float= ondalıklı sayılar
print(averagePoint+5)

isVerified = True    #/False #boolean
print(isVerified)

print(type(text))
print(type(studentCount))
print(type(studentCount1))
print(type(averagePoint))
print(type(isVerified))

#  matematiksel ve mantıksal
number = 10
print(10+10)
print(number+number)

print(10-10)
print(number-5)

print(number/2)

print(number * 3)

print(number%3)   #mod operatörü : bölümünden kalan sayıyı verir

#mantıksal operatörler  --- karşılaştırma operatörleri
print(10==number) #true
print(number==11) #false

print(number!=10) #false
print(number!=11) #true

print(number>10)   #false
print(number>= 10) #true
print(number<= 10) #true


#string interpolation => metin birleştirme 
text = "Hello"
kullaniciAdi="irem"

totalText=text+" "+kullaniciAdi
print(totalText)
print(text+" "+kullaniciAdi)

totalText = "{message} Sayın {name}".format(message=text, name=kullaniciAdi)
print(totalText)

#f-string
totalText =f"Hoşgeldiniz {kullaniciAdi}"
print(totalText)

totalText =f"{text} {kullaniciAdi} Hoşgeldiniz"
print(totalText)
















