import requests

URL =  'https://api-web.nhle.com/v1/player/8479318/game-log/20232024/3'

r = requests.get(url= URL)

data = r.json()

print(len(data['gameLog']))

# 8479318