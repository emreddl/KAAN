#!/usr/bin/env python
# coding: utf-8

# In[15]:


deger = (22.5, 23.1, 21.8, 19.5, 18.9, 20.2, 22.7, 24.3, 25.6, 26.2, 25.8, 24.9, 23.7, 22.4, 21.1, 20.8, 19.9, 18.7, 19.2, 20.5, 21.9, 23.3, 22.8, 21.5)
konfor = []
klima = 0 
ısıtıcı = 0 
boyut = 0

for x in deger:
    if x >24 or x<20:
        konfor.append(boyut)

    if x >25:
        klima+=1
        
    if x <18:
        ısıtıcı+=1

    boyut+=1


fark = max(deger) - min(deger)
ort = sum(deger) / len(deger)

print(f'İdeal oda sıcaklığı 20-24 derece arasıdır. Bu aralıkta olmayan saatler: {konfor}')
print(f'18 derece altında ısıtıcı çalışıyor.çalışan saat sayısı:{ısıtıcı}')
print(f'25 derece üzeri sıcaklıklarda klima çalışıyor.Çalışan saat sayısı: {klima}')
print(f'Gün içindeki en yüksek ve en düşük sıcaklık arasındaki fark: {fark}')
print(f'Günlük ortalama sıcaklığı hesapla: {ort}')

