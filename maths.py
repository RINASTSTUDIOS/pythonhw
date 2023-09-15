import math_module_by_rinast
import time
print("RINAST trafından yapılan basit math.py'ye hoş geldiniz!!")                                                                                                                                                                                                                                          
time.sleep(0.7)
x = input("Hangi özelliği kullanmak istersiniz;asalkontrol,kökalma,faktoriyel,üs,ortalama,dairealanı,daireçevresi,hipotenüs?")
time.sleep(0.5)
if x == "asalkontrol":
    sonuc = math_module_by_rinast.prime()
    print(sonuc)
elif x == "kökalma":
    y = input("Sayıyı ve kök değerini giriniz(arada virgül olmalı):")
    z = y.split(",")
    sayi = int(z[0])
    kok = int(z[1])
    sonuc = math_module_by_rinast.root(sayi,kok)
    print(sonuc)
elif x == "faktoriyel":
    sayi = int(input("Sayıyı giriniz:"))
    sonuc = math_module_by_rinast.factorial(sayi)
    print(sonuc)
elif x == "üs":
    y = input("Sayıyı ve üssü giriniz(arada virgül olmalı):")
    z = y.split(",")
    sayi = int(z[0])
    us = int(z[1])
    sonuc = math_module_by_rinast.power(sayi,us)
    print(sonuc)
elif x == "ortalama":
    sayilar = input("Sayıları arada virgülle giriniz:")
    s = sayilar.split(",")
    sonuc = math_module_by_rinast.av(s)
    print(sonuc)
elif x == "dairealanı":
    giris = input("Dairenin yarıçapını ve seçtiğiniz pi değerini giriniz(arada - olsun):")
    degerler = giris.split("-")
    sonuc = math_module_by_rinast.circle_area(degerler[0],degerler[1])
    print(sonuc)
elif x == "daireçevresi":
    giris = input("Dairenin yarıçapını ve seçtiğiniz pi değerini giriniz(arada - olsun):")
    degerler = giris.split("-")
    sonuc = math_module_by_rinast.circle_perimeter(degerler[0],degerler[1])
    print(sonuc)
elif x == "hipotenüs":
    giris = input("Üçgenin kenar değerlerini giriniz(arada - olsun):")
    degerler = giris.split("-")
    sonuc = math_module_by_rinast.hipotenus(degerler[0],degerler[1])
    print(sonuc)
else:
    print("Yanlış girdi")