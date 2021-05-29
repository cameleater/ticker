import requests
import json
from datetime import date, datetime
import os

kc = requests.get('https://kiwi-coin.com/api/order_book/')
kcResponse = json.loads(kc.content)

print(kcResponse['bids'])
print("=================")
print("=================")
print("=================")
print("=================")
print("=================")
print(kcResponse['asks'])
