# When user send a message

from conf.texts4messages import *

def rtext(bot, update):
    user_text = update.message.text.lower()

    if user_text == "olá" or user_text == "ola" :   bot_text = HELLO_MESSAGE
    elif user_text == "ow" or user_text == "ou" :   bot_text = "-tário."
    else:                                           bot_text = "Não entendi."

    bot.send_message(
        chat_id = update.message.chat_id,
        text=bot_text
    )
