import requests

class Message:
    TOKEN = "5712332102:AAFsFwOcE08hjVpEk7g1IJ5Rih9VQKoUEnU"
    CHATID = -511328095

    def sendMessage(msg):
        url = f'https://api.telegram.org/bot{Message.TOKEN}/sendMessage?chat_id={Message.CHATID}&text={msg}'
        try:
            requests.get(url).json()
        except Exception as e:
                print(e)