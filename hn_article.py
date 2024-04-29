import requests
import json

url = f'https://hacker-news.firebaseio.com/v0/item/31353677.json'

r = requests.get(url)
request_data = r.json()
request_information = json.dumps(request_data, indent = 4)

print(request_information)