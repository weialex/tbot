from telegram.ext import CommandHandler, Filters, MessageHandler, Updater, CallbackQueryHandler

#from conf.settings import TELEGRAM_TOKEN
from conf.texts4messages import DONT_ACCEPT_MEDIA
from commands import *
from messages import *

import requests
import re

def who(bot, update):
    nome=str(update.message.from_user.first_name)

    bot.send_message(
        chat_id = update.message.chat_id,
        text="Pois não, "+nome+"?"
    )

def raudio(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text=DONT_ACCEPT_MEDIA
    )

def ranimation(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text=DONT_ACCEPT_MEDIA
    )

def button(bot, update):
    query = update.callback_query

    if(query.data >= '1' and query.data <= '6'):
        text=sendIdolGif(bot, update, query)

    query.edit_message_text(text=text)

def mydispatcher(disp):
    disp.add_handler(CommandHandler('start', start))
    disp.add_handler(CommandHandler('http', http_cats, pass_args=True))
    disp.add_handler(CommandHandler('who', who))
    disp.add_handler(CommandHandler('help', help, pass_args=True))
    disp.add_handler(CommandHandler('about', about))
    disp.add_handler(CommandHandler('decision', undecided, pass_args=True))
    disp.add_handler(CommandHandler('idol', idol))
    disp.add_handler(CommandHandler('teste', teste))
    disp.add_handler(CommandHandler('motivacional', motivacional))

    disp.add_handler(CallbackQueryHandler(button))

    disp.add_handler(MessageHandler(Filters.text, rtext))
    disp.add_handler(MessageHandler(Filters.audio | Filters.voice, raudio))
    disp.add_handler(MessageHandler(Filters.animation | Filters.video, ranimation))

    #command don't expected
    disp.add_handler(MessageHandler(Filters.command, unknown))
