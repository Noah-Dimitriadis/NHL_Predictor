import requests
from pprint import pprint

URL =  'https://api-web.nhle.com/v1/score/2023-11-10'

r = requests.get(url= URL)

data = r.json()

pprint(data)

