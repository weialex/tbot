from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import TELEGRAM_TOKEN, HTTP_CATS_URL
from conf.texts4messages import *

def start(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text=START_WELCOME
    )

def http_cats(bot, update, args):
    bot.sendPhoto(
        chat_id = update.message.chat_id,
        photo = HTTP_CATS_URL + args[0]
    )

def help(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text=HELP_MESSAGE
    )
    bot.sendPhoto(
        chat_id = update.message.chat_id,
        photo = "https://p2.trrsf.com/image/fget/cf/940/0/images.terra.com/2018/07/19/pudim-de-geladeira.jpg"
    )

def about(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text=ABOUT_MESSAGE
    )

def unknown(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text=UNKNOWN_MESSAGE
    )
    bot.sendAnimation(
        chat_id = update.message.chat_id,
        animation="https://i.imgur.com/KxOR0LC.gif"
    )

def hello(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text=HELLO_MESSAGE
    )

def who(bot, update):
    nome=str(update.message.from_user.first_name)

    bot.send_message(
        chat_id = update.message.chat_id,
        text=nome
    )

def rtext(bot, update):

    bot.send_message(

    )

def raudio(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text=DONT_ACCEPT_MEDIA
    )
    bot.sendAnimation(
        chat_id = update.message.chat_id,
        animation="https://media1.tenor.com/images/eb1b27863813653543914d222ceb9cd0/tenor.gif?itemid=5548554"
    )

def ranimation(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text=DONT_ACCEPT_MEDIA
    )
    bot.sendAnimation(
        chat_id = update.message.chat_id,
        animation="https://external-preview.redd.it/QJl4sfn1r2lsRglVwNk9B5UiPuxh4skAU2BRVq4zDsQ.gif?format=mp4&s=e0aaa48d55c67053be16639e131a0017944fecc5"
    )

def main():
    updater = Updater(token = TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('http', http_cats, pass_args=True))

    dispatcher.add_handler(CommandHandler('who', who))

    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('about', about))


    #dispatcher.add_handler(MessageHandler('oi', hello))

    #command don't expected
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    dispatcher.add_handler(MessageHandler(Filters.text, rtext))

    dispatcher.add_handler(MessageHandler(Filters.audio | Filters.voice, raudio))
    dispatcher.add_handler(MessageHandler(Filters.animation | Filters.video, ranimation))

    #start the bot
    updater.start_polling()

    # works until ctrl+c
    updater.idle()

if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()
