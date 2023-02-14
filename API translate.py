import requests

API_KEY = 'trnsl.1.1.20221005T023701Z.1ff518fb3d503dc2.691dbb525fed832f91e6930befc07ec82fc75e96'
url ='https://translate.yandex.net/api/v1.5/tr.json/translate'

Texto = input("Digite o texto a ser traduzido: ")
params = dict(key=API_KEY, text=Texto, lang="pt-en")

response = requests.get(url, params=params)

json = response.json()['text'][0]

print(json)
