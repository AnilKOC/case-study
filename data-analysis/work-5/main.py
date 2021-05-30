import pandas as pd

df = pd.read_csv('tckn_ad.csv')
tckn=""
ad=""

query = input("Enter the search values: ")
query = query.split("#")

for i in query:
    try:
        a=int(i)
        tckn=i
    except:
        ad=i

tckn_query=""
ad_query=""
try:
    tckn_query = df.loc[df['TCKN '] == int(tckn)]
except:
    pass

try:
    ad_query = df.loc[df['AD'] == ad]
except:
    pass

tckn_new = []
try:
    for i in tckn_query.iloc:
        tckn_new.append([i[0],i[1],i.name])
except: pass

ad_new = []
try:
    for i in ad_query.iloc:
        ad_new.append([i[0],i[1],i.name])
except: pass

for i in tckn_new:
    if i not in ad_new:
        ad_new.append(i)

df = pd.DataFrame (ad_new,columns=['TCKN','AD','ID'])
df.to_csv('tckn_ad_final.csv', index=False)