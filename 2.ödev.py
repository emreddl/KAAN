"""
1- Bir liste içindeki sayıların karelerini alarak yeni bir liste oluşturun.
[1,2,3,4,5,6,7,8,9,10]
"""
listelimiz = [1,2,3,4,5,6,7,8,9,10]

newOne = [a*a for a in listelimiz]
print(newOne)

"""
2- İç içe for döngüleri kullanarak 1’den 10’a kadar olan sayıların çarpım tablosunu
oluşturan bir program yazın. Her sayının 1’den 10’a kadar olan çarpımlarını ekrana yazdırın.
Çıktı düzenli ve okunaklı olmalıdır.
"""
for a in range(1,10):
    for b in range(1,10):
        c = a*b
        print(f"{a} ve {b}'nin çarpımı sonucu: {c}")
print("\n")

"""
3- Bilgisayarın 1-100 arasında rastgele tuttuğu bir sayıyı kullanıcının 
tahmin etmeye çalıştığı bir program yazın. Kullanıcıya ipucu verin( daha büyük/daha küçük), maksimum 10 deneme hakkı tanıyın, doğru tahminde oyunu sonlandırın.
"""

import random
dogruSayi = random.randint(1,100)
tahminEdilen = int(input("Tahminde bulununuz: "))

while dogruSayi != tahminEdilen:
    if dogruSayi > tahminEdilen:
        print("Tahmininiz düşük")

    elif dogruSayi < tahminEdilen:
        print("Tahmininiz yüksek")

    tahminEdilen = int(input("Tahminde bulununuz: "))

print("Doğru tahmin! :*")
print("\n")










"""
4- Kullanıcıdan 10 adet sayı alan ve bu sayılardan sadece tek olanların toplamını hesaplayan bir program yazın. Her tek sayı eklendiğinde bilgi mesajı versin, sonunda tek sayıların toplamını göstersin. (İpucu: Çift sayıları continue komutu ile atlayabilirsiniz.)
"""
toplam = 0
listeSayi = []
sayac = 0
while sayac < 10:
    b = input(f"{sayac+1}.sayiyi giriniz: ")
    listeSayi.append(int(b))
    sayac += 1

for a in listeSayi:
    if a % 2 != 0:
        toplam += a

print("Girilen tüm tek sayıların toplamı: {}".format(toplam))
print("\n")






"""5- Verilen 2 listeyi zip fonksiyonu ile birleştirerek index ve değerleri birlikte yazdırın.
[“Ali”, ”Ayşe”, ”Mehmet”, ”Zeynep”]
[25, 30, 35, 28]
"""
isimler = ["Ali", "Ayşe", "Mehmet", "Zeynep"]
yaslar = [25, 30, 35, 28]

for a in enumerate(zip(isimler, yaslar)):
    print(a)

print("\n")



"""
6- Range fonksiyonunu kullanarak;
a) 1’den 100’e kadar olan çift sayıların toplamını bulun.
b) 50’den geriye doğru 40’a kadar olan sayıları yazdırın.
"""
toplam = 0
deger = [*range(1,100)]
for a in deger:
    if a%2 == 0:
        toplam +=a
print(toplam)
print("\n")

for a in range(50,40,-1):
    print(a)