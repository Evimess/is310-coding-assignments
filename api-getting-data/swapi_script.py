import requests
import json

url = "https://swapi.dev/api/people/1/"
response = requests.get(url)
response_data = response.json()
with open("luke.json","w") as json_file:
    json.dump(response_data, json_file)