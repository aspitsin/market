import requests
from bot_settings import token


def get_bot_updates():
    last_offset = 0
    url = "https://api.telegram.org/bot456429804:" + token + "/getupdates"
    params = {"offset": last_offset + 1}
    result = requests.get(url, params=params)
    pydict = result.json()
    return pydict['result']


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


def main():
    while True:
        rate_btc = get_btc()
        rate_eth = get_eth()
        for result in get_bot_updates():
            text = result['message']['text']
            chat = result['message']['chat']['id']
            print(text, chat)
            if text == '/btc':
                print(send_mess(chat, rate_btc))
            elif text == '/eth':
                print(send_mess(chat, rate_eth))
            else:
                print(send_mess(chat, "Type /btc or /eth "))


print(main())
