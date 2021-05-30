import pandas as pd
import re

IL_ILCE = {
    'IL':['ANKARA','ANKARA','ANKARA','İSTANBUL'],
    'ILCE':['ÇANKAYA','ALTINDAĞ','ETİMESGUT','ŞİŞLİ']
}
il_ilce = pd.DataFrame(IL_ILCE)

ILCE_MAHALLE = {
    'ILCE':['ÇANKAYA','ÇANKAYA','ÇANKAYA','ÇANKAYA','ŞİŞLİ','ŞİŞLİ','ŞİŞLİ'],
    'MAHALLE':['KAVAKLIDERE','ESAT','AYRANCI','CUMHURİYET','BOZKURT','ESKİŞEHİR','CUMHURİYET']
}
ilce_mahalle = pd.DataFrame(ILCE_MAHALLE)

OKUL_MAHALLE = {
    'OKUL_ADI':['Kavaklıdere İÖO','Etimesgut Anadolu Lisesi','Cumhuriyet Lisesi','Zafer İlkokulu'],
    'MAHALLE':['Kavaklıdere Mah.','Eryaman Mah.','Bozkurt Mah.','Cumhurİyet Mah.']
}
okul_mahalle = pd.DataFrame(OKUL_MAHALLE)

mahalle = []
for i in okul_mahalle['MAHALLE']:
    mahalle.append(i[:-5].upper())

okul_mahalle.pop('MAHALLE')
okul_mahalle.insert(1,"MAHALLE",mahalle,True)

ilce = []
for i in range(len(okul_mahalle['MAHALLE'])):
    ilce.append([])
    query = ilce_mahalle.loc[ilce_mahalle['MAHALLE'] == str(okul_mahalle['MAHALLE'][i])]
    if len(query) >= 2:
        for j in query['ILCE']:
            ilce[i].append(j)
    elif len(query)==1:
        ilce[i] = (query['ILCE'].values.tolist())

il = []
for i in range(len(ilce)):
    il.append([])
    if len(ilce[i]) == 1:
        query = il_ilce.loc[il_ilce['ILCE'] == ilce[i][0]]
        il[i] = query['IL'].values.tolist()
    if len(ilce[i]) >= 2:
        for j in range(len(ilce[i])):
            query = il_ilce.loc[il_ilce['ILCE'] == ilce[i][j]]
            il[i].append(query['IL'].values.tolist()[0])

okul_mahalle = pd.DataFrame(OKUL_MAHALLE)
okul_mahalle.insert(2,"ILCE",ilce,True)
okul_mahalle.insert(3,"IL",il,True)

okul_mahalle.to_csv('okul_mahalle_final.csv', index=False)