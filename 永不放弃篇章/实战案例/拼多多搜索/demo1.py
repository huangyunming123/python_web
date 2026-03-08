import requests


response = requests.get("http://localhost:5211/api/data")
json = response.json()['result']
print(json)