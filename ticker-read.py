import requests
import json
import configparser
import sys
from datetime import date, datetime
import os
import blep
from blep import Bl3pApi

# init blep calls
#-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
config = configparser.RawConfigParser()

if len(sys.argv) == 2:
    config.read(sys.argv[1])
else:
    config.read('example.cfg')

public_key = config.get('bl3p', 'public_key')  # ........-....-....-....-............
secret_key = config.get('bl3p', 'secret_key')  # (long string with a-z/A-Z/0-9 and =)

blep_call = Bl3pApi('https://api.bl3p.eu/1/', public_key, secret_key)
# print(blep_call.get_balances())
# print(blep_call.full_depth('BTC'))

#create log file with todays date as the file name
#-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
today = date.today()
currentDate = today.strftime("%Y%m%d")
# C:\Users\jordan\project\cryptoBot\logs
filePath = "C:\\Users\\jordan\\project\\cryptoBot\\logs\\" + currentDate
f = open(filePath,"a+")
fHigh = open(filePath + "-high","a+")
# fHighRead = open(filePath + "-high","r")



#get currency rates because we display prices in USD
#-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
curr = requests.get("http://api.openrates.io/latest?base=USD&symbols=EUR,NZD")
currencyResponse = json.loads(curr.content)
nzToUsdRate = currencyResponse["rates"]["NZD"]
eurToUsdRate = currencyResponse["rates"]["EUR"]
# print(nzToUsdRate)
# print(eurToUsdRate)

#get current bid and ask price from kc public api
timeNow = str(datetime.now())
kc = requests.get('https://kiwi-coin.com/api/ticker/')
kcResponse = json.loads(kc.content)

kcBidToUsd = kcResponse["bid"] / nzToUsdRate
kcAskToUsd = kcResponse["ask"] / nzToUsdRate

f.write(timeNow + "\n")
f.write("KIWI-COIN \n")
f.write("SELL AT: " + str(kcBidToUsd) + "\n")
f.write("BUY AT: " + str(kcAskToUsd) + "\n\n")

# blep public api prices
blep = requests.get('https://api.bl3p.eu/1/BTCEUR/ticker')
if blep.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(cd.status_code))

blepResponse = json.loads(blep.content)
# print(blepResponse)

blepBidToUsd = blepResponse["bid"] / eurToUsdRate
blepAskToUsd = blepResponse["ask"] / eurToUsdRate

f.write(timeNow + "\n")
f.write("BLEP \n")
f.write("SELL AT: " + str(blepBidToUsd) + "\n")
f.write("BUY AT: " + str(blepAskToUsd) + "\n\n")
f.write("============================== \n\n")

# Price comparison logic
#-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
if kcAskToUsd < blepBidToUsd:
    f.write("======== PROFITABLE TRADE ========= \n")
    f.write("BUY ON KIWI-COIN FOR " + str(kcAskToUsd) + "\n")
    f.write("AND SELL ON BL3P FOR " + str(blepBidToUsd) + "\n")
    percentageProfit = ((blepBidToUsd - kcAskToUsd) / blepBidToUsd) * 100
    f.write("FOR A PERCENTAGE GAIN OF: " + str(percentageProfit) + "%\n")
    f.write("=================================== \n\n\n\n\n")

    fHigh.write("FOR A PERCENTAGE GAIN OF: " + str(percentageProfit) + "%\n")

    if percentageProfit > 0:
        fHigh.write("% IS WORTH. ATTEMPT TRADE FOR: " + str(percentageProfit) + "% PROFIT \n")
        Bl3pApi.add_order()

    else:
        fHigh.write("TRADE NOT WORTH \n")
else:
    print("no trades available to buy on kiwi-coin")
    print(blep_call.add_order('EUR', 'ask', ))

if blepAskToUsd < kcBidToUsd:
    f.write("======== PROFITABLE TRADE ========= \n")
    f.write("BUY ON BL3P FOR " + str(blepAskToUsd) + "\n")
    f.write("AND SELL ON KIWI-COIN FOR " + str(kcBidToUsd) + "\n")
    percentageProfit = ((kcBidToUsd - blepAskToUsd) / kcBidToUsd) * 100
    f.write("FOR A PERCENTAGE GAIN OF: " + str(percentageProfit) + "\n")
    f.write("=================================== \n\n\n\n\n")

    fHigh.write("FOR A PERCENTAGE GAIN OF: " + str(percentageProfit) + "%\n")

    if percentageProfit > 4:
        fHigh.write("% IS WORTH. ATTEMPT TRADE FOR: " + str(percentageProfit) + "% PROFIT \n")
    else:
        fHigh.write("TRADE NOT WORTH \n")
else:
    print("no trades available to buy on bl3p")
