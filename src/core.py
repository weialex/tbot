from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import TELEGRAM_TOKEN, HTTP_CATS_URL
from conf.texts4messages import *
from operations import *


def main():
    updater = Updater(token = TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    mydispatcher(dispatcher)

    #start the bot
    updater.start_polling()

    # works until ctrl+c
    updater.idle()

if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()
