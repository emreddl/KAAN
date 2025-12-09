"""
1- Kullanıcıdan alınan n sayısına kadar Fibonacci serisi oluşturan bir generator fonksiyon yazın. Daha sonra bu serideki:
- Tek sayıları filtreleyin
- Kalan çift sayıların karekökünü alın
- Sonuçları lambda ve map ile işleyip liste olarak döndürün
Örnek: n=10 → Fibonacci: [0,1,1,2,3,5,8,13,21,34]
"""
"""
def fibo_func(deger):
    if deger <= 0:
        return None
    elif deger == 1:
        sonuc = [0]
    else:
        sonuc = [0,1]
        for x in range(2, deger):
            sonuc.append(sonuc[x-1] + sonuc[x-2])

        ciftListe = [*filter(lambda x: x %2 ==0,sonuc)]
        return ciftListe

def kareKokAl(liste):
    return list(map(lambda x: x**0.5,liste))


belirle = True
while belirle:
    try:
        deger = int(input("Bir sayı giriniz."))
        belirle = False
    except ValueError:
        print("Sayi giriniz!")
a = fibo_func(deger)
donenListe = kareKokAl(a)

print(f"Girdiginiz degere göre döndürülen fibonnaci listesi: {donenListe}\n")
"""

"""
2- Verilen bir listedeki tüm elemanları recursive olarak düzleştiren (flatten) bir program yazın.
Liste iç içe listeler içerebilir.
Gereksinimler:
- Recursive lambda kullanın (Y-combinator)
- Map/filter ile implemente edin
- Sadece sayıları koruyun, diğer tipleri filtreleyin
Örnek: [1, [2, [3, 4]], 5, [6, 'a']] → [1, 2, 3, 4, 5, 6]
"""

"""
Y = lambda f: (lambda g: f(lambda *args: g(g)(*args)))(
    lambda g: f(lambda *args: g(g)(*args)))

flatten_lambda = Y(
    lambda k: lambda liste:
    [] if len(liste) == 0 else (
            (k(liste[0]) if isinstance(liste[0], list) else [liste[0]]) + k(liste[1:])
    )
)
def sayilari_flatten_et(gelen_liste):
    duz_liste = flatten_lambda(gelen_liste)
    kopya_liste = list(map(lambda x: x, duz_liste))

    sadece_sayilar = list(
        filter(
            lambda x: isinstance(x, (int, float)),
            kopya_liste
        )
    )
    return sadece_sayilar

liste = [1, [2, [3, 4]], 5, [6, 'a']]
sonuc = sayilari_flatten_et(liste)
print(sonuc) 

"""

"""
3- Gerçek zamanlı veri işleme sistemi:
- Kullanıcıdan sürekli sayı girmesini isteyin
- Her girişte:
 * Sayıyı bir stream'e ekleyin
* Son 5 sayının ortalamasını hesaplayın (moving average)
 * Standart sapma hesaplayın
 * Anomaly detection (3 sigma kuralı)
- 'quit' yazınca program sonlansın
Gereksinimler:
- Generator functions for stream processing
- Map/reduce operations on sliding window
- Lambda for statistical calculations
- Try-except for invalid inputs
- Functional state management (no global variables)
Örnek:
Input: 10, 12, 15, 11, 9, 100 (anomali), 13
Output: MA: 11.4, Std: 2.1, Anomaly: 100 detected!
"""

"""
import math
def girisDeger():
    deger = []
    standart_sapma = 0
    avg = 0
    quit = True
    tekrar = 2
    while quit:
        metin = input("Sayi giriniz(Cikis yapmak icin quit yazınız): ")
        if metin.lower() =="quit":
            print("Sistemden çıkış yaptınız!")
            break
        else:
            try:
                deger.append(int(metin))
                if tekrar < 1:
                    if deger[-1] > (avg + 3*standart_sapma) or deger[-1] < (avg - 3*standart_sapma):
                        print(f"Anomaly detected!: {deger[-1]}")

            except ValueError:
                print("Sayi girdisi yapmıyorsunuz!\n")

        if len(deger) > 1 and len(deger) < 5:
            avg = sum(deger) / len(deger)
            print(f"Şu ana kadar girilen değerlerin ortalaması: {avg}")
            for a in deger:
                standart_sapma += (a-avg)**2
            standart_sapma = math.sqrt(standart_sapma / (len(deger)-1))
            print("Standart sapma: {} \n \n".format(standart_sapma))

        elif len(deger) > 5:
            avg = sum(deger[-5:]) / 5
            print(f"Son 5 elemanın girilen değerlerin ortalaması: {avg}")
            for a in deger:
                standart_sapma += (a-avg)**2
            standart_sapma = math.sqrt(standart_sapma / (len(deger)-1))
            print("Standart sapma: {}".format(standart_sapma))

        tekrar-=1

    return 0

girisDeger()
"""

"""
4- Kullanıcıdan bir sayı girmesini isteyen ve bu sayının karekökünü hesaplayan bir program yazın.
- Negatif sayı girilirse uygun hata mesajı verin
- Sayı yerine metin girilirse uygun hata mesajı verin
- Try-except blokları kullanın
"""

"""
belirlec = True
while belirlec:
    try:
        girdii = input("Bir sayi giriniz(Çıkış için çıkış yazın):")
        if girdii.lower() == "çıkış":
            break
        sayi = int(girdii)
        if sayi < 0:
            raise ValueError("Lütfen pozitif bir sayi giriniz!!!!\n")
        sayi = math.sqrt(sayi)
        print("Girdiginiz sayinin karekoku: {} \n".format(sayi))

    except Exception as err:
            print("Hata: ",err)
    except TypeError:
            print("Metin değil sayı giriniz.")
"""

"""
5- Dört işlem yapan bir hesap makinesi fonksiyonu yazın.
- Toplama, çıkarma, çarpma, bölme işlemleri
- Kullanıcıdan işlem tipi ve sayıları input ile alın
- Bölme işleminde sıfıra bölme hatasını try-except ile yakalayın
- Geçersiz işlem girilirse uygun mesaj verin
- Lambda ifadeleri kullanarak işlemleri tanımlayın
"""

"""
def hesap_mak():
    girdi1 = 0
    girdi2 = 0
    while True:
        islem = input("Yapmak istediğiniz işlemi yazınız[Çarpma,Bölme,Toplama,Çıkarma]: \n")
        islem = islem.lower()

        if not any(kelime in islem.lower() for kelime in ['bölme', 'çarpma', 'toplama', 'çıkarma']):
            print("Geçersiz işlem. Lütfen geçerli bir işlem seçiniz!!\n")
            continue
        girdi1 = int(input("1.sayıyı giriniz\n"))
        girdi2 = int(input("2.sayıyı giriniz\n"))
        if islem.lower == "bölme":
            try:
                if girdi2 == 0:
                    raise ValueError("Bölme işleminde bölen 0 olamaz!!\n")
                bolme = lambda x,y: x/y
                print("İki sayının bölümü{}:".format(bolme(girdi1,girdi2)))
            except ValueError as er:
                print("Hatanız: ",er)

        if islem.lower() == "toplama":
            toplama = lambda x,y: x+y
            print("İki sayının toplamı:{}\n".format(toplama(girdi1,girdi2)))

        if islem.lower() == "çıkarma":
            cıkarma = lambda x,y: x-y
            print("İki sayının farkı:{}\n".format(cıkarma(girdi1, girdi2)))

        if islem.lower() == "çarpma":
            carpma = lambda x,y: x*y
            print("İki sayının çarpımı:{}\n".format(carpma(girdi1, girdi2)))

hesap_mak()
"""

"""
6- Bir isim listesindeki tüm isimleri büyük harfe çeviren ve başına "Sayın " ekleyen bir program yazın.
Örnek: ["ali", "ayşe", "mehmet"] → ["Sayın ALİ", "Sayın AYŞE", "Sayın MEHMET"]
- Lambda ve map kullanın
- Kullanıcıdan virgülle ayrılmış isimler alın
"""

"""
isimListe = []
while True:
    try:
        isim = input("İsimleri giriniz(Bitirmek için bitti yazın): ")
        if isim.lower() == "bitti":
            break
        isimListe.append(isim)
    except TypeError:
        print("Metin gir!")

def buyukHarf(liste):
    sayinEkle = list(map(lambda x: "Sayin " + x.upper(), liste))
    return sayinEkle

yeniListe =buyukHarf(isimListe)

print ("Yeni liste: {}".format(yeniListe))
"""

