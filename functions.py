#definiton tanımlama
def ortalamaHesapla() :
    final=100
    vize=85
    ortalama=(vize*0.4)+(final*0.6)
    print(ortalama)

def ortalamaHesapla2():
    final=100
    vize=85
    ortalama=(vize*0.4)+(final*0.6)
    return ortalama

ortalamaHesapla()
print(ortalamaHesapla2())

def ortalamaHesapla3(vize : float,final : float):
    return (vize*0.4)+(final*0.6)

print(ortalamaHesapla3(78,93))
