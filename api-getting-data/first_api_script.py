import requests
import apikey
import json

apikey.save("dpla_key", "api_key")

dpla_api_key = apikey.load("dpla_key")
url = "https://api.dp.la/v2/items?q=kittens&api_key=" + dpla_api_key

response = requests.get(url)
response_data = response.json()
with open("dpla_kittens.json","w") as json_file:
    json.dump(response_data, json_file)

