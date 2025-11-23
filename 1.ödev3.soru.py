#!/usr/bin/env python
# coding: utf-8

# In[14]:


def kullanıcı(kAdi1,şifre1,mail1,yas1):
    a = 0
    dogrulukListe = [False,False,False,False]
    belirleyici = False
    s = []
    s = list(şifre1)
    yas = int(yas1)

    if yas>13:
        dogrulukListe[0] = True

    if len(şifre1) >=6 and any(ch.isdigit() for ch in şifre1):
        dogrulukListe[1] = True

    if "@" in mail1:
        dogrulukListe[2] = True
        
    if len(kAdi1)>=3:
        dogrulukListe[3] = True
    
    while a < len(dogrulukListe):
        if dogrulukListe[a] != True:
           belirleyici = False
           break
        else:
            belirleyici = True
            a+=1
    return belirleyici

kAdi = input("Kullanıcı adı giriniz")
şifre = input("Şifre giriniz")
mail = input("Mail adresi giriniz")
yas = input("Yasınızı giriniz")
    
sonuc = kullanıcı(kAdi,şifre,mail,yas)
print(sonuc)


# In[ ]:




