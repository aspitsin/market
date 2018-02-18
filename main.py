import requests
from bot_settings import token


def get_bot_updates():
    url = "https://api.telegram.org/bot456429804:" + token + "/getupdates"
    result = requests.get(url)
    pydict = result.json()
    return pydict['result']


def last_text():
    result = get_bot_updates()
    text = result[-1]['message']['text']
    return text


def last_chat_id():
    result = get_bot_updates()
    chat = result[-1]['message']['chat']['id']
    return chat


def send_mess(chat, text):
    url = "https://api.telegram.org/bot456429804:" + token
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + '/sendMessage', data=params)
    return response


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


text = last_text()
chat = last_chat_id()
rate_btc = get_btc()
rate_eth = get_eth()

print(text, chat)

if text == 'btc':
    print(send_mess(chat, rate_btc))
elif text == 'eth':
    print(send_mess(chat, rate_eth))
else:
    print(send_mess(chat, text))
