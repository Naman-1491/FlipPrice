import django
import os
import sys

sys.path.append('/home/jainam/Documents/FlipPrice/')
sys.path.append('/home/jainam/Documents/FlipPrice/Telegram')
os.environ['DJANGO_SETTINGS_MODULE'] = 'FlipPrice.settings'
django.setup()
from config import Secrets
# from api.config import Secretsuser_data = TelegramUser.objects.get(id=user.id)
from Telegram.models import TelegramUser
from telegram import Update, ReplyKeyboardMarkup
from logging import basicConfig, getLogger, INFO
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters

reply_keyboard = [['/start', '/help'], ['/url', '/price'], ['/stop']]


def start_command(update: Update, _: CallbackContext) -> None:
    user = update.effective_user
    try:
        if TelegramUser.objects.filter(id=user.id):
            pass
        else:
            TelegramUser.objects.create(id=user.id, name=user.full_name, username=user.username)
    except Exception:
        pass

    reply_text = [f"Hi {user.first_name}!", "Now please enter the URL of flipkart product."]
    for reply in reply_text:
        update.message.reply_text(reply)


def help_command(update: Update, _: CallbackContext) -> None:
    reply_text = """Enter url of Flipkart product. I will track price of that product!\n\nList of commands:\n1. 
    /start - It will start the bot.\n2. /help - It will show you this prompt.\n3. /price - It will show the current 
    price of the product.\n4. /url - It will show the product url.\n5. /stop - It will delete all the data and stops 
    the bot """

    update.message.reply_text(reply_text, reply_markup=ReplyKeyboardMarkup(reply_keyboard))


def price_command(update: Update, _: CallbackContext) -> None:
    from locale import currency, setlocale, LC_MONETARY
    setlocale(LC_MONETARY, '')
    user = update.effective_user
    user_data = TelegramUser.objects.get(id=user.id)
    if user_data.price is not None:
        reply_text = f"Today's price for you product is: {currency(user_data.price, grouping=True)}"
    else:
        reply_text = f"Please enter the Flipkart's product url!"

    update.message.reply_text(reply_text, reply_markup=ReplyKeyboardMarkup(reply_keyboard))


def url_command(update: Update, _: CallbackContext) -> None:
    user = update.effective_user
    user_data = TelegramUser.objects.get(id=user.id)
    if user_data.url is not None:
        reply_text = [f"Current tracking the price of the product given below:", user_data.url]
    else:
        reply_text = [f"Please enter the Flipkart's product url!"]

    for reply in reply_text:
        update.message.reply_text(reply, reply_markup=ReplyKeyboardMarkup(reply_keyboard))


def stop_command(update: Update, _: CallbackContext) -> None:
    user = update.effective_user
    user_data = TelegramUser.objects.get(id=user.id)
    user_data.url = None
    user_data.price = None
    user_data.save()
    reply_text = [f"Your old product's url is deleted.", f"Please enter new Flipkart's product url."]
    for reply in reply_text:
        update.message.reply_text(reply, reply_markup=ReplyKeyboardMarkup(reply_keyboard))


def messenger(update: Update, _: CallbackContext) -> None:
    from responses import Responses
    responses = Responses()
    user = update.effective_user
    replies = responses.get_reply(update.message.text, user)
    for reply in replies:
        update.message.reply_text(reply)


if __name__ == '__main__':
    print("Bot Running.")
    basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - (message)s',
        level=INFO
    )

    logger = getLogger(__name__)
    secrets = Secrets()

    updater = Updater(secrets.get_token(), use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(CommandHandler('price', price_command))
    dispatcher.add_handler(CommandHandler('url', url_command))
    dispatcher.add_handler(CommandHandler('stop', stop_command))
    dispatcher.add_handler(MessageHandler(Filters.text, messenger))

    updater.start_polling()
    updater.idle()
    print("Bot Stopped.")
