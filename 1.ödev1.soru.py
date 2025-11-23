#!/usr/bin/env python
# coding: utf-8

# In[5]:


listecik = [
    {"isim":"Emre","soyisim":"Yılmaz", "vize":70,"final":30},
    {"isim":"Furkan","soyisim":"Boz","vize":10,"final":20},
    {"isim":"Yiğit","soyisim":"Doğam","vize":79,"final":81},
    {"isim":"Deniz","soyisim":"Sevdi","vize":100,"final":80},
    {"isim":"Sudem","soyisim":"Emir", "vize":90, "final":90}
]

for kişi in listecik:
    ort = kişi["vize"]*0.4 + kişi["final"]*0.6
    if ort>=50:
        kişi["durum"]= "Geçti"
    else: 
        kişi["durum"]= "Kaldı"

print(listecik)


# In[ ]:




