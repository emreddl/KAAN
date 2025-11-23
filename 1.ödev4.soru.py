#!/usr/bin/env python
# coding: utf-8

# In[2]:


def func(sayi1,sayi2):
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    a = sayi1 + sayi2
    b = sayi1 - sayi2
    if sayi2 != 0:
        c = sayi1 / sayi2
    else:
        print ( "Bölünemez")
    d = sayi1*sayi2

    return a,b,c,d


sayi1 = input("Sayi giriniz")
sayi2 = input("Sayi giriniz")


donenDeger = func(sayi1,sayi2)
print(donenDeger)


# In[ ]:




