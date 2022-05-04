import django
import os
import sys
sys.path.append('/home/jainam/Documents/FlipPrice/')
sys.path.append('/home/jainam/Documents/FlipPrice/Telegram')
os.environ['DJANGO_SETTINGS_MODULE'] = 'FlipPrice.settings'
django.setup()
from Telegram.models import TelegramUser


class Responses:
    def __init__(self):
        self.__reply = list()

    def __check_url_validity(self, url):
        from re import search, compile
        pattern = r"((http|https)://)(www\.)?flipkart\.com.*"
        regex = compile(pattern)
        if search(regex, url):
            return True
        else:
            return False

    def __get_price(self, user, url):
        from requests import get
        from html import unescape
        from bs4 import BeautifulSoup
        link = get(url)
        html = unescape(link.text)
        parser = BeautifulSoup(html, 'html.parser')
        tag = parser.find('div', {"class": "_30jeq3 _16Jk6d"})
        price = tag.string
        return price

    def __update_url(self, user, url):
        user_data = TelegramUser.objects.get(id=user.id)
        user_data.url = url
        user_data.save()
        return self.__get_price(user, url)

    def __update_price(self, user, price):
        price = price[1:].replace(',', '')
        price = int(price)
        user_data = TelegramUser.objects.get(id=user.id)
        user_data.price = price
        user_data.save()

    def get_reply(self, message:str, user):
        if 'http' in message or 'flipkart' in message:
            if self.__check_url_validity(message):
                self.__reply.append("Hurray! you've entered valid url.")
                self.__reply.append("Now, I will keep my eyes on it👀.")
                price = self.__update_url(user, message)
                self.__reply.append(f"Current Price is: {price}")
                self.__update_price(user, price)
            else:
                self.__reply.append("Please enter url of flipkart product only!")

        elif 'who are you' in message.lower():
            self.__reply.clear()
            self.__reply.append("I'm FkartBot!😇")

        elif "hi" in message.lower() or "hii" in message.lower() or "hello" in message.lower() or "hey" in message.lower():
            self.__reply.clear()
            self.__reply.append("Hii there!")

        elif "thanks" in message.lower() or "thank you" in message.lower() or "thank-you" in message.lower() or "thankyou" in message.lower():
            self.__reply.clear()
            self.__reply.append("It's my pleasure!😊")

        elif "bye" in message.lower():
            self.__reply.clear()
            self.__reply.append("Bye-Bye👋\nHave a nice day!!")

        else:
            self.__reply.clear()
            self.__reply.append("I didn't get it!😕")

        return self.__reply
