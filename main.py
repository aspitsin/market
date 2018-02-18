import requests
from bot_settings import token


def get_bot_updates():
    url = "https://api.telegram.org/bot456429804:" + token + "/getupdates"
    result = requests.get(url)
    pydict = result.json()
    return pydict['result']


result = get_bot_updates()

for message in result:
    text = message['message']['text']
    chat_id = message['message']['chat']['id']


def send_mess(chat, text):
    url = "https://api.telegram.org/bot456429804:" + token
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

#--------------------------------------------------------------------------------------------------


def get_btc():
    url = "https://api.cryptonator.com/api/ticker/btc-usd"
    result = requests.get(url)
    pydict = result.json()
    btc = pydict['ticker']['price']
    return btc


def get_eth():
    url = "https://api.cryptonator.com/api/ticker/eth-usd"
    result = requests.get(url)
    pydict = result.json()
    eth = pydict['ticker']['price']
    return eth


print(get_btc(), get_eth())
