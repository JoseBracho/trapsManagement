import requests

class Message:
    TOKEN = "0"
    CHATID = 0

    def sendMessage(msg):
        url = f'https://api.telegram.org/bot{Message.TOKEN}/sendMessage?chat_id={Message.CHATID}&text={msg}'
        try:
            requests.get(url).json()
        except Exception as e:
                print(e)
