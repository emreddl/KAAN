#!/usr/bin/env python
# coding: utf-8

# In[26]:


metin = "Python, Guido van Rossum tarafından 1991 yılında geliştirilmiş bir programlama dilidir. Python, okunabilirliği ve basit sözdizimi ile öne çıkar. Dilin tasarım felsefesi, kod okunabilirliğini vurgular ve bu da onu yeni başlayanlar için ideal kılar. Python, web geliştirme, veri analizi, yapay zeka, bilimsel hesaplama ve otomasyon gibi birçok alanda kullanılır. Python'un geniş kütüphane ekosistemi, geliştiricilere güçlü araçlar sunar. Python topluluğu çok aktiftir ve sürekli olarak dilin gelişimine katkıda bulunur. Python programlama dilini öğrenmek, yazılım dünyasında birçok kapı açar."
metin = metin.lower()

işaret = [",", ".", "'"]

kelime = [c for c in metin if c not in işaret]
metin = "".join(kelime)

print(metin)

listem = metin.split()

sözlük = {}

for x in listem:
    if x not in sözlük:
        sözlük[x] = 1
    else:
        sözlük[x] += 1

listeHali = list(sözlük.items())

listeHali.sort(key = lambda x : x[1], reverse=True)
print("\n\n")

a = 0
while a<3:
    print(listeHali[a])
    a+=1


# In[ ]:




