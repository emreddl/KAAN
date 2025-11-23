#!/usr/bin/env python
# coding: utf-8

# In[5]:


def fonksi(yas1,gelir1):
    yas = int(yas1)
    gelir = int(gelir1)

    if yas <18:
        print("Yaşınız kredi için uygun değil.")

    if yas>= 18 and yas<=65 and gelir>5000:
        print("Kredi onaylandı")

    if yas>= 18 and yas<=65 and gelir<5000:
        print("Gelir yetersiz")

    if yas>65:
        print("Yasınız kredi için uygun değil")

    return 


yas = input("Yas Gir")

gelir = input("Gelir Gir")

fonksi(yas,gelir)



# In[ ]:




