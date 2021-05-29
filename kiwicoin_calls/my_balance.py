import time
import math
import hmac
import hashlib
import requests
UserId = "AVWQ-RZ7E-YM95"
Key = "FrC21XMWO9YwioblJdrOU7ORwmWpXLgI"
Secret = "8hhSyxhFl2ioYotI0rdyBJExqRFnOhEt"
Nonce = math.trunc(time.time())
Message = str(Nonce) + str(UserId) + Key + ";balance"
Signature = hmac.new(Secret, msg=Message, digestmod=hashlib.sha256).hexdigest().upper()
R = requests.post("https://kiwi-coin.com/api/balance/", data={'key': Key, 'signature': Signature, 'nonce': Nonce})
print(R.status_code, R.reason, R.text)
