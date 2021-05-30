import pandas as pd
import re
#import requests


df = pd.read_csv('mail.csv', encoding = "ISO-8859-1", engine='python')

mail_service_list=[]
for mail in df.EMAIL:
  company = ""
  selector = 0
  for i in mail:
    if i==".": selector = 0
    if selector==1: company += i.lower()
    if i=="@": selector = 1
  mail_service_list.append(company)

df.insert(2,"MAIL_Service",mail_service_list,True)

'''
company_list = []

for i in range(len(df.MAIL)):

  mail = df.MAIL[i]
  mail = mail.lover()
  service = df.MAIL_Servıce[i]

  response1 = requests.get("https://api-url/",mail)
  response2 = requests.get("https://api-url/",service)
  
  if mail in response1.json() or mail in response2.json():
      company_list.append(service)
  else:
      company_list.append(None)

df.pop('Mail_Service')
df.insert(2,"Company",company_list,True)
'''

df.to_csv('mail_final.csv', index=False)