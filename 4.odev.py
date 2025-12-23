""""
1- Banka Hesap Sistemi (Class + Dunder Methods)
BankaHesabi adında bir class oluşturun:
__init__ : hesap_no, bakiye, hesap_turu (vadeli/vadesiz), hesap_acilis_tarihi(datetime kullanın)
__str__: Hesap bilgilerini döndürsün
__add__: iki hesabın bakiyelerini toplayıp yeni bir bakiye değeri döndürmeli
para_cek, para_yatir methodları (para_cek methodu yeterli bakiye yoksa uyarı vermeli)
hesap_raporu methodu: tüm işlem geçmişini tarih-saat bilgisi ile göstermeli
Örnek: print(hesap1) à”12345 nolu hesap – Bakiye: 1000 TL – Tür: Vadesiz”
"""

"""
import datetime
import time
class BankaHesabi:
    islem = []
    vadeli = 0
    vadesiz = 0

    def __init__(self, hesap_no, bakiye, hesap_turu, hesap_acilis_tarihi):
        self.hesap_turu = hesap_turu
        self.vadeli_bakiye = 0
        self.vadesiz_bakiye = 0

        if self.hesap_turu.lower() == "vadesiz":
            self.vadesiz_bakiye = bakiye
        elif self.hesap_turu.lower() == "vadeli":
            self.vadeli_bakiye = bakiye

        self.islem = []
        self.hesap_no = hesap_no
        self.hesap_acilis_tarihi = hesap_acilis_tarihi

    def __str__(self):
        return f"HesapNo: {self.hesap_no}, Tür: {self.hesap_turu}, Açılış: {self.hesap_acilis_tarihi}"

    def __add__(self, diger):
        return (self.vadeli_bakiye + self.vadesiz_bakiye) + (diger.vadeli_bakiye + diger.vadesiz_bakiye)

    def para_cek(self, tutar):
        if self.hesap_turu.lower() == "vadesiz":
            if tutar > self.vadesiz_bakiye:
                print("Çekmek istediğiniz miktarda paranız bulunmuyor.")
                a = time.time()
                okunur = datetime.datetime.fromtimestamp(a)
                olay = f"{okunur} vaktinde {tutar} tutarında {self.hesap_no} no'lu hesabınızdan para çekilme işlemi yetersiz bakiyeden kaynaklı olarak başarısız olmuştur.Güncel bakiye {self.vadesiz_bakiye}"
                self.islem.append(olay)

            else:
                a = time.time()
                okunur = datetime.datetime.fromtimestamp(a)
                self.vadesiz_bakiye -= tutar
                olay = f"{okunur} vaktinde {tutar} tutarında {self.hesap_no} no'lu hesabınızdan para çekilmiştir. Güncel bakiye {self.vadesiz_bakiye}"
                self.islem.append(olay)

        elif self.hesap_turu.lower() == "vadeli":
            print("Vadeli hesaptan para çekemezsiniz faiz kaybı olur!")

    def para_yatir(self, tutar):
        a = time.time()
        okunur = datetime.datetime.fromtimestamp(a)  # FIX

        if self.hesap_turu.lower() == "vadesiz":
            self.vadesiz_bakiye += tutar
            olay = f"{okunur} vaktinde {tutar} tutarında {self.hesap_no} no'lu hesabınıza para yatırılmıştır. Güncel bakiye {self.vadesiz_bakiye}"
        else:
            self.vadeli_bakiye += tutar
            olay = f"{okunur} vaktinde {tutar} tutarında {self.hesap_no} no'lu hesabınıza para yatırılmıştır. Güncel bakiye {self.vadeli_bakiye}"

        self.islem.append(olay)

    def hesap_raporu(self):
        for a in self.islem:
            print(a)


a = BankaHesabi(23533253, 1000, "Vadesiz", datetime.datetime.now())
a.para_cek(300)
a.para_yatir(900)
a.para_cek(3000)
a.hesap_raporu()
"""

"""
2- Öğrenci Not Sistemi (Inheritance + Collections)
Ogrenci base class ve LisansOgrencisi, YuksekLisansOgrencisi subclass’ları oluşturun.
Ogrenci: ad, soyad, ogrenci_no, ders_notlari (dict)
not_ekle: ders adı ve not listesi alacak, Counter ile not istatistiği tutsun
ortalama_hesaplama : math modülü ile yuvarlama (math.ceil ya da math.floor)
LisansOgrencisi: ortalama hesaplama methodunu override edip farklı formül kullanacak
YuksekLisansOgrencisi: Not değerlendirme kriterleri farklı olacak.
Örnek: ogrenci1.not_ekle(“Matematik”, [85, 90, 78])
"""

"""
import math
import collections
class Ogrenci():

    def __init__(self,ad,soyad,ogrenci_no,ders_notlari):
        self.ad = ad
        self.soyad = soyad
        self.ogrenci_no = ogrenci_no
        self.ders_notlari = {}

    def not_ekle(self,ders_adi,not_liste):
        if isinstance(not_liste, int):
            not_liste = [not_liste]

        if ders_adi not in self.ders_notlari:
            self.ders_notlari[ders_adi] = {
                "notlar" : [],
                "istatistik" : collections.Counter()
            }
        self.ders_notlari[ders_adi]["notlar"].extend(not_liste)
        self.ders_notlari[ders_adi]["istatistik"].update(not_liste)

    def ortalama_hesaplama(self):
        toplam = 0
        ort = 0
        for a in self.ders_notlari.keys():
            notlar = self.ders_notlari[a]["notlar"]
            toplam = 0
            for b in notlar:
                toplam += int(b)
        ort = toplam / len(notlar)
        math.floor(ort)
        print(f"{self.ders_notlari[a]} dersinin ortalaması {ort}")

class LisansOgrencisi(Ogrenci):
    def ort(self):
        top = 0
        sayi = 0
        for a in self.ders_notlari.keys():
            for b in self.ders_notlari[a].values():
                top += b
            sayi = top / len(self.ders_notlari[a].values())+5
            math.ceil(sayi)
            print(f"{self.ders_notlari[a]} dersinin ortalaması {sayi}")

class YuksekLisansOgrencisi(Ogrenci):
    def notlar(self):
        ortalama = self.ortalama_hesaplama()
        if ortalama >90:
            print("AA")
        elif ortalama >80 and ortalama <90:
            print("BA")
        elif ortalama >70 and ortalama <80:
            print("BB")
        else:
            print("KALDIN!")

ogrenci = Ogrenci("Emre","Çermez",100020303,[35,432,453])
ogrenci.not_ekle("Türkce",90)
ogrenci.not_ekle("Türkce",[90,70])
ogrenci.ortalama_hesaplama()
"""

"""
3- Dosya Yöneticisi ( File Operations + Random)
Dosya ve klasör işlemleri için kapsamlı bir yönetici sınıfı. Dosya oluşturma, okuma, arama ve yedekleme işlemleri yapabilmeli.
dosya_olustur methodu: random modülü ile rastgele isimli dosya oluşturacak.
dosya_oku_regex methodu: re modülü ile dosya içinde pattern arayacak
klasör_tarama methodu: os modülü ile belirtilen klasördeki tüm dosyaları listeleyecek.
__len__ methodu: klasördeki dosya sayısını döndürecek.
"""
"""
import random
import os
import re
class ManagementClass():
    def __init__(self, klasor_yolu="."):
        self.klasor_yolu = klasor_yolu
        os.makedirs(self.klasor_yolu, exist_ok=True)

    alfabe= [
        'A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    def _rastgele_isim(self, uzunluk=8):
        return "".join(random.choice(self.letters) for _ in range(uzunluk))

    def dosya_olustur(self, uzunluk=8, uzanti=".txt", icerik=""):
        isim = self._rastgele_isim(uzunluk)
        dosya_adi = isim + uzanti
        tam_yol = os.path.join(self.klasor_yolu, dosya_adi)
        fd = os.open(tam_yol, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o666)
        try:
            os.write(fd, icerik.encode("utf-8"))
        finally:
            os.close(fd)
        self.son_dosya = tam_yol
        return tam_yol

    def dosya_oku_regex(self, dosya_yolu, pattern):
        boyut = os.stat(dosya_yolu).st_size
        fd = os.open(dosya_yolu, os.O_RDONLY)
        try:
            veri = os.read(fd, boyut)
        finally:
            os.close(fd)
        text = veri.decode("utf-8")
        eslesmeler = []
        for match in re.finditer(pattern, text):
            eslesmeler.append({
                "match": match.group(),
                "start": match.start(),
                "end": match.end()
            })
        return eslesmeler

    def tarama(self):
        dosyalar = []
        for isim in os.listdir(self.klasor_yolu):
            tam_yol = os.path.join(self.klasor_yolu, isim)
            if os.path.isfile(tam_yol):
                dosyalar.append(tam_yol)
        return dosyalar

    def __len__(self):
        return len(self.tarama()
"""

"""
4- E-Ticaret Sistemi (OOP Composition)
E-ticaret sitesi için ürün, müşteri ve sipariş yönetim sistemi.
Urun class: isim, fiyat, stok(property decorator ile kontrol), barkod(random modülü ile oluşturulacak)
Musteri class: ad, email, sepet (ürün listesi), sipariş geçmişi
Siparis class: sipariş no (random), sipariş tarihi (datetime), toplam tutar
odeme_yap methodu: math modülü ile KDV hesaplayacak (%18)
stok_guncelle methodu: Ürün satın alındığında stokları güncelleyecek.
__contains__ methodu: müşterinin sepetinde belirli ürün olup olmadığını kontrol edecek.
"""
"""
import random
import math
from datetime import datetime

class Urun:
    def __init__(self, isim, fiyat, stok):
        self.isim = isim
        self.fiyat = fiyat
        self.stok = stok
        self.barkod = self.rastgeleBarkod()

    @property
    def stok(self):
        return self.stok

    @stok.setter
    def stok(self, yeniDeger):
        if yeniDeger < 0:
            raise ValueError("Stok eksi olamaz!")
        self.stok = yeniDeger

    def rastgeleBarkod(self):
        sayilar = [str(random.randint(0, 9)) for _ in range(13)]
        return "".join(sayilar)

    def __str__(self):
        return f"{self.isim} | Fiyat: {self.fiyat} TL | Stok: {self.stok}"

class Musteri:
    def __init__(self, ad, email):
        self.ad = ad
        self.email = email
        self.sepet = []
        self.siparisGecmisi = []

    def sepeteUrunEkle(self, urun):
        self.sepet.append(urun)

    def siparisVerme(self):
        if not self.sepet:
            print("Sepet boş, sipariş verilemez.")
            return None

        siparis = Siparis(self, self.sepet)
        siparis.stokGuncelleme()
        self.siparisGecmisi.append(siparis)
        self.sepet = []
        return siparis

    def __contains__(self, urun):
        return urun in self.sepet

class Siparis:
    def __init__(self, musteri, urunListesi):
        self.musteri = musteri
        self.urunler = list(urunListesi)
        self.siparisNo = self.rastgeleSiparisNo()
        self.siparisTarihi = datetime.now()
        self.toplamTutar = self.toplamHesaplama()

    def rastgeleSiparisNo(self):
        return random.randint(100000, 999999)

    def toplamHesaplama(self):
        return sum(urun.fiyat for urun in self.urunler)

    def odemeYapma(self):
        kdv = self.toplamTutar * 0.18
        kdv = math.floor(kdv * 100) / 100

        genelToplam = self.toplamTutar + kdv
        return genelToplam, kdv

    def stokGuncelleme(self):
        for urun in self.urunler:
            urun.stok -= 1

    def __str__(self):
        return (f"Sipariş No: {self.siparisNo} | "
                f"Tarih: {self.siparisTarihi} | "
                f"Toplam: {self.toplamTutar} TL")
"""

"""
5- Quiz Uygulaması (Collections + Random)
Zamanlı quiz uygulaması. Soruları rastgele seçmeli, süre tutmalı ve detaylı rapor oluşturmalı.
soru_bankasi:  Soru, cevap, zorluk seviyesi içeren sözlük
soru_sec methodu: random.sample ile belirtilen sayıda rastgele soru seçecek
quiz_baslat methodu: time.time ile süre başlatacak.
cevap_kontrol methodu: collections.Counter ile doğru/yanlış istatistiği tutacak.
rapor_olustur methodu: datetime ile detaylı quiz raporu oluşturacak.
puan_hesapla methodu: math modülü ile zorluk katsayılarına göre puan hesaplayacak.
"""
"""
from random import sample
from collections import Counter
from datetime import datetime
import time
import math

class SinavMotoru:
    # soru havuzu: list of dict (sende dict-of-dict idi)
    soruHavuzu = [
        {
            "kod": "Q01",
            "metin": "Python'da liste eleman sayısını veren fonksiyon hangisidir?",
            "cevap": "len",
            "zorluk": "Kolay"
        },
        {
            "kod": "Q02",
            "metin": "Türkiye'nin uluslararası telefon kodu kaçtır? (Örn: 90)",
            "cevap": "90",
            "zorluk": "Orta"
        },
        {
            "kod": "Q03",
            "metin": "IPv4 adresi kaç bitten oluşur? (Sadece sayı yaz)",
            "cevap": "32",
            "zorluk": "Orta"
        },
        {
            "kod": "Q04",
            "metin": "SQL'de benzersiz (unique) kayıtları seçmek için kullanılan ifade nedir?",
            "cevap": "DISTINCT",
            "zorluk": "Kolay"
        }
    ]
    def __init__(self):
        self.oturumKaydi = []
        self.toplamSure = 0.0
        self.ozet = Counter()
        self.toplamPuan = 0

    def normalize(self, x):
        return str(x).strip().lower()

    def katsayi(self, zorluk):
        return {"Kolay": 1, "Orta": 2, "Zor": 3}.get(zorluk, 1)

    def rastgeleSec(self, adet):
        if adet < 1:
            raise ValueError("Soru sayısı en az 1 olmalı.")
        if adet > len(self.soruHavuzu):
            raise ValueError(f"En fazla {len(self.soruHavuzu)} soru seçebilirsin.")
        return sample(self.soruHavuzu, k=adet)

    def baslat(self, adet):
        self.oturumKaydi.clear()
        self.ozet = Counter()
        self.toplamPuan = 0
        self.toplamSure = 0.0
        sorular = self.rastgeleSec(adet)
        print("Sınav başlıyor...")
        input("Hazırsan Enter'a bas: ")
        t0 = time.time()
        for s in sorular:
            print("\nSoru:", s["metin"])
            kullanici = input("Cevabın: ")
            dogruMu = (self.normalize(kullanici) == self.normalize(s["cevap"]))
            self.oturumKaydi.append({
                "kod": s["kod"],
                "dogruMu": dogruMu,
                "zorluk": s["zorluk"]
            })
        t1 = time.time()
        self.toplamSure = t1 - t0
        print(f"\nSınav bitti! Süre: {self.toplamSure:.1f} saniye")
    def kontrolEt(self):
        etiketler = ["Doğru" if k["dogruMu"] else "Yanlış" for k in self.oturumKaydi]
        self.ozet = Counter(etiketler)
        return self.ozet

    def puanla(self):
        puan = 0
        for k in self.oturumKaydi:
            if k["dogruMu"]:
                puan += 10 * self.katsayi(k["zorluk"])
        self.toplamPuan = math.floor(puan)
        return self.toplamPuan

    def rapor(self):
        if not self.ozet:
            self.kontrolEt()
        if self.toplamPuan == 0 and any(x["dogruMu"] for x in self.oturumKaydi):
            self.puanla()

        zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n--- RAPOR ---")
        print("Tarih:", zaman)
        print(f"Süre: {self.toplamSure:.1f} saniye")
        print("Doğru:", self.ozet.get("Doğru", 0))
        print("Yanlış:", self.ozet.get("Yanlış", 0))
        print("Puan:", self.toplamPuan)

if __name__ == "__main__":
    app = SinavMotoru()
    app.baslat(3)
    app.kontrolEt()
    app.puanla()
    app.rapor()
"""

"""
6- Personel Yönetim Sistemi (Advanced OOP)
Şirket personel yönetimi için gelişmiş sistem. Farklı personel türleri için inheritance kullanacak.
Personel base class: ad, soyad, maas, departman, ise_baslama_tarihi (datetime)
zam_hesapla methodu: datetime ile kıdem hesaplayıp zam oranı belirleyecek
izin_hesapla methodu: datetime.timedelta ile çalışılan gün sayısına göre izin hesaplayacak
Yonetici subclass: Ek olarak sorumlu_oldugu_kisiler listesi ve bonus hesaplama
Gelistirici subclass: Teknoloji stack listesi ve proje bazlı prim hesaplama
eq methodu: İki personelin maaşlarını karşılaştıracak
gt methodu: Hangi personelin daha uzun süredir çalıştığını kontrol edecek.
Örnek: personel1 = Yonetici("Mehmet", "Demir", 20000, "IT", "2020-03-15") personel2 = Gelistirici("Zeynep", "Kaya", 15000, "Yazılım", "2021-06-20") print(f"Kıdem: {personel1 > personel2}") # gt test print(f"Zam oranı: {personel1.zam_hesapla()}")
"""

"""
from datetime import date
class Personel():
    def __init__(self, ad, soyad, maas, departman, iseBaslamaTarihi=None):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.departman = departman

        if iseBaslamaTarihi is None:
            self.iseBaslamaTarihi = date.today()
        else:
            # date objesi geliyorsa direkt ata
            if isinstance(iseBaslamaTarihi, date):
                self.iseBaslamaTarihi = iseBaslamaTarihi
            # string gelirse "YYYY-MM-DD" formatını kabul et
            elif isinstance(iseBaslamaTarihi, str):
                self.iseBaslamaTarihi = date.fromisoformat(iseBaslamaTarihi)
            # tuple/list gelirse (yıl, ay, gün) kabul et
            elif isinstance(iseBaslamaTarihi, (tuple, list)) and len(iseBaslamaTarihi) == 3:
                self.iseBaslamaTarihi = date(iseBaslamaTarihi[0], iseBaslamaTarihi[1], iseBaslamaTarihi[2])
            else:
                raise TypeError("iseBaslamaTarihi date / 'YYYY-MM-DD' / (yil, ay, gun) olmalidir.")

    def kidemYili(self):
        bugun = date.today()
        fark = bugun - self.iseBaslamaTarihi
        yil = fark.days // 365
        return yil

    def zamHesaplama(self):
        kidem = self.kidemYili()

        if kidem < 1:
            oran = 0.00
        elif kidem < 3:
            oran = 0.05
        elif kidem < 5:
            oran = 0.10
        else:
            oran = 0.15

        yeniMaas = self.maas * (1 + oran)
        self.maas = yeniMaas
        return oran, yeniMaas

    def izinHesapla(self):
        bugun = date.today()
        calismaSuresi = bugun - self.iseBaslamaTarihi
        calisilanGun = calismaSuresi.days
        izinGunu = calisilanGun // 30
        return izinGunu

    def __eq__(self, other):
        if not isinstance(other, Personel):
            return NotImplemented
        return self.maas == other.maas

    def __gt__(self, other):
        if not isinstance(other, Personel):
            return NotImplemented
        # Daha erken başlayan daha kıdemli olsun istiyorsan bu doğru
        return self.iseBaslamaTarihi < other.iseBaslamaTarihi

class Yonetici(Personel):
    def __init__(self, ad, soyad, maas, departman, iseBaslamaTarihi=None, sorumluOlduguKisiler=None):
        super().__init__(ad, soyad, maas, departman, iseBaslamaTarihi)

        if sorumluOlduguKisiler is None:
            sorumluOlduguKisiler = []
        self.sorumluOlduguKisiler = sorumluOlduguKisiler

    def bonusHesaplama(self):
        kidem = self.kidemYili()
        kisiSayisi = len(self.sorumluOlduguKisiler)

        oran = kidem * 0.02 + kisiSayisi * 0.01
        bonus = self.maas * oran
        return bonus

class Gelistirici(Personel):
    def __init__(self, ad, soyad, maas, departman, iseBaslamaTarihi=None, teknolojiStack=None):
        super().__init__(ad, soyad, maas, departman, iseBaslamaTarihi)

        if teknolojiStack is None:
            teknolojiStack = []
        self.teknolojiStack = teknolojiStack
        self.projeler = []

    def projeEkleme(self, projeAdi, zorluk):
        self.projeler.append({
            "ad": projeAdi,
            "zorluk": zorluk})

    def primHesaplama(self):
        katsayi = {
            "kolay": 0.02,
            "orta": 0.04,
            "zor": 0.06
        }
        toplamPrim = 0

        for proje in self.projeler:
            zorluk = str(proje["zorluk"]).lower()
            oran = katsayi.get(zorluk, 0.02)
            toplamPrim += self.maas * oran
        return toplamPrim

personel1 = Yonetici("Ahmet", "Turp", 20000, "IT", "2000-03-15")
personel2 = Gelistirici("Fevzi", "Koşuyolu", 15000, "Yazılım", "2017-06-20")

print(f"Kıdem: {personel1 > personel2}")
print(f"Zam oranı: {personel1.zamHesaplama()}")
"""