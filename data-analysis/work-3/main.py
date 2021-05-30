import pandas as pd
import re

IS_ADRESI = [
    "Tugay Yolu Cad. No:60 Maltepe",
    "İnkılap Mah. Küçüksu Cd. No 6 Ümraniye",
    "Soğanlık Mah. Muş Sk. No 63 Kartal"
]
EV_ADRESI = [
    "Tugay Yolu Caddesi No60 MALTEPE",
    "İnkılap Mahallesi Küçüksu Caddesi No 6 Ümraniye",
    "Soğanlık Mah. Muş Sk. No 61 Kartal"
]

cadde = {
    'cad':'cd',
    'caddesi':'cd',
}
mahalle = {
    'mahallesi':'mah',
}

def optimization(new_adres):
    for i in range(len(new_adres)):
        for j in range(len(new_adres[i])):
            try:
                if cadde[new_adres[i][j]]:
                    new_adres[i][j] = cadde[new_adres[i][j]]
            except:
                None
            try:
                if mahalle[new_adres[i][j]]:
                    new_adres[i][j] = mahalle[new_adres[i][j]]
            except:
                None
    return new_adres

def cleaning(adres):
    new_adres = []
    for line in adres:
        new_line=re.split('[ .:,]', line.lower())
        stint = re.compile("([a-zA-Z]+)([0-9]+)")
        new = []
        for i in new_line:
            if i:
                if stint.match(i):
                    last = stint.match(i).groups()
                    for j in last:
                        new.append(j)
                else:
                    new.append(i)

        new_adres.append(new)
    return new_adres

def main():
    result = cleaning(IS_ADRESI)
    is_adresi_final = optimization(result)
    result2 = cleaning(EV_ADRESI)
    ev_adresi_final = optimization(result2)
    same=[]
    for i in range(len(is_adresi_final)):
        same.append(1)
        for j in range(len(is_adresi_final[i])):
            if is_adresi_final[i][j] not in ev_adresi_final[i]:
                same[i]=0
    print(same)
    print(is_adresi_final)
    print(ev_adresi_final)
    frame = {
        'IS_ADRESI':IS_ADRESI,
        'EV_ADRESI':EV_ADRESI,
        'ORTAK':same
    }
    df = pd.DataFrame(frame)
    df.to_csv('is_ev_adres_final.csv', index=False)

if __name__=="__main__":
    main()