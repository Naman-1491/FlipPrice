import django
import os
import sys

sys.path.append('/home/jainam/Documents/FlipPrice/')
sys.path.append('/home/jainam/Documents/FlipPrice/Telegram')
os.environ['DJANGO_SETTINGS_MODULE'] = 'FlipPrice.settings'
django.setup()
import requests
from time import sleep
from html import unescape
from bs4 import BeautifulSoup
from Telegram.config import Secrets
from Telegram.models import TelegramUser


class Tracker:

    def __init__(self):
        self.__users = None
        self.__secrets = Secrets()

    def __create_user_object(self):
        self.__users = TelegramUser.objects.all()

    def scrapper(self):
        self.__create_user_object()
        print("Tracking running.")
        for user in self.__users:
            link = requests.get(user.url)
            html = unescape(link.text)
            del link
            parser = BeautifulSoup(html, 'html.parser')
            del html
            tag = parser.find('div', {"class": "_30jeq3 _16Jk6d"})
            del parser
            price = int(tag.string[1:].replace(',', ''))
            if user.price > price:
                user.price = price
                user.save()
                msgs = [f"Attention! Price for you product is decreased.", f'Grab it now!',
                        f"Today's Price: {tag.string}"]
                del tag
                del price
                for msg in msgs:
                    url = f'https://api.telegram.org/bot{self.__secrets.get_token()}/sendMessage?chat_id={user.id}&text={msg}'
                    requests.get(url)
            else:
                pass

            print("Waked up!")
            sleep(10)
        # delete objects to free space
        del self.__users
        del user
        # delete objects to free space
        print('Tracking stopped.')


if __name__ == '__main__':
    while True:
        track = Tracker()
        track.scrapper()
        del track
        sleep(10*60)
