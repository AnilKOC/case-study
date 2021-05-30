import pandas as pd

adress_list = [
    "Tugay Yolu Cad. No:60 12537489122 Maltepe",
    "İnkılap Mah. 88372637771 Küçüksu Cd. No 6 Ümraniye",
    "11293888122 Soğanlık Mah. Muş Sk. No 63 Kartal",
    "Bilezikçi sk 147 Şişli İstanbul 12229386"
]

kimlik_list = []
adress_new = []
for i in range(len(adress_list)):
    new_line = adress_list[i].split()
    kimlik_list.append(None)
    for j in new_line:
        try:
            number = int(j)
            if len(j)==11:
                kimlik_list[i]=int(j)
                new_line.remove(j)
        except:
            None
    final_line = ""
    for i in new_line:
        final_line+=i+" "
    adress_new.append(final_line[:-1])

d = {'Adres': adress_new, 'Kimlik_No': kimlik_list}
df = pd.DataFrame(data=d)

df.to_csv('adres_final.csv', index=False)