import requests
import pandas as pd
URL = 'https://v6.exchangerate-api.com/v6/ae0dc30f0ea3cbca428c873d/latest/EUR'
response = requests.get(URL)
json = response.json()
ExRa = pd.DataFrame(json)
Med = ExRa.conversion_rates.median()
print('Median      ',Med)
info = ExRa.conversion_rates.describe()
print(info)
i = input('Max range of exchange rates shown? ')
try:
    num = int(i)
except:
    print('Invaid input')
    exit()
if num < 0:
    print('Invalid input')
    exit()
OpList = ExRa.conversion_rates[ExRa.conversion_rates <= num]
print(OpList)
OpList.to_csv('Exchange_rates')