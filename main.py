import requests
from bot_settings import token


def get_bot_updates():
    url = "https://api.telegram.org/bot456429804:" + token + "/getupdates"
    result = requests.get(url)
    pydict = result.json()
    return pydict['result']


result = get_bot_updates()

for messages in result:
    text = messages['message']['text']
    chat_id = messages['message']['chat']['id']
    print(text, chat_id)
