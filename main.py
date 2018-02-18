import requests
from bot_settings import token


def get_bot_updates():
    url = "https://api.telegram.org/bot456429804:" + token + "/getupdates"
    result = requests.get(url)
    pydict = result.json()
    return pydict['result']


def last_update():
    pass


def last_text():
    result = get_bot_updates()
    text = result[-1]['message']['text']
    return text


def last_chat_id():
    result = get_bot_updates()
    chat = result[-1]['message']['chat']['id']
    return chat_id


def send_mess(chat, text):
    url = "https://api.telegram.org/bot456429804:" + token
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + '/sendMessage', data=params)
    return response


def example():
    chat = last_chat_id()
    text = last_text()
    print(text)
    if text == 'btc':
        print(get_btc())
    print send_mess(chat, text)


print(example())


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
