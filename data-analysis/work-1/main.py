import pandas as pd
import re

df = pd.read_csv('telefon.csv')

alan_kodu = {
    322:'Adana',
    416:'Adıyaman',
    272:'Afyon',
    472:'Ağrı',
    382:'Aksaray',
    312:'Ankara',
    242:'Antalya',
    478:'Ardahan',
    466:'Artvin',
    256:'Aydın',
    266:'Balıkkesir',
    378:'Bartın',
    488:'Batman',
    458:'Bayburt',
    228:'Bilecik',
    426:'Bingöl',
    434:'Bitlis',
    374:'Bolu',
    248:'Burdur',
    224:'Bursa',
    286:'Çanakkale',
    376:'Çankırı',
    364:'Çorum',
    258:'Denizli',
    412:'Diyarbakır',
    380:'Düzce',
    284:'Edirne',
    850:'Çoğrafi-850',
    424:'Elazığ',
    446:'Erzincan',
    442:'Erzurum',
    222:'Eskişehir',
    342:'Gaziantep',
    454:'Giresun',
    456:'Gümüşhane',
    438:'Hakkâri',
    326:'Hatay',
    476:'Iğdır',
    246:'Isparta',
    216:'İstanbul (Anadolu)',
    212:'İstanbul (Avrupa)',
    232:'İzmir',
    344:'Kahramanmaraş',
    370:'Karabük',
    338:'Karaman',
    474:'Kars',
    366:'Kastamonu',
    352:'Kayseri',
    318:'Kırıkkale',
    288:'Kırklareli',
    386:'Kırşehir',
    348:'Kilis',
    262:'Kocaeli',
    332:'Konya',
    274:'Kütahya',
    422:'Malatya',
    236:'Manisa',
    482:'Mardin',
    324:'Mersin',
    252:'Muğla',
    436:'Muş',
    384:'Nevşehir',
    388:'Niğde',
    452:'Ordu',
    328:'Osmaniye',
    464:'Rize',
    264:'Sakarya',
    362:'Samsun',
    484:'Siirt',
    368:'Sinop',
    346:'Sivas',
    414:'Şanlıurfa',
    486:'Şırnak',
    282:'Tekirdağ',
    356:'Tokat',
    462:'Trabzon',
    428:'Tunceli',
    276:'Uşak',
    432:'Van',
    226:'Yalova',
    354:'Yozgat',
    372:'Zonguldak'
}

gsm_kodu=[501, 505, 506, 507, 551,552, 553, 554, 555, 559,540, 541, 542, 543, 544, 545, 546, 547, 548, 549,	530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 561]

new_numbers = []
number_status = []
for number in df.TELEFON:
    new = re.sub(r'#.*$', "", number)
    new = re.sub(r'\D', "", new)
    if new[0]=="0":
      new=new[1:]
    if new[0:2]=="90":
      new=new[2:]
    if int(new[0:3]) in alan_kodu:
      number_status.append(alan_kodu[int(new[0:3])])
    elif int(new[0:3]) in gsm_kodu:
      number_status.append("GSM")
    else:
        number_status.append(None)
    new_numbers.append(int(new))

df.pop("TELEFON")
df.insert(1,"TELEFON",new_numbers,True)
df.insert(2,"TELEFON_DURUM",number_status,True)

df.to_csv('telefon_final.csv', index=False)