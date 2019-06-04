from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import TELEGRAM_TOKEN, HTTP_CATS_URL
from conf.texts4messages import *
from operations import *
from random import seed, randint

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

def who(bot, update):
    nome=str(update.message.from_user.first_name)

    bot.send_message(
        chat_id = update.message.chat_id,
        text="Pois não, "+nome+"?"
    )

def rtext(bot, update):
    user_text = update.message.text.lower()

    if user_text == "olá" or user_text == "ola" :   bot_text = HELLO_MESSAGE
    elif user_text == "ow" or user_text == "ou" :   bot_text = "-tário."
    else:                                           bot_text = "Não entendi."

    bot.send_message(
        chat_id = update.message.chat_id,
        text=bot_text
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

def undecided(bot, update, args):
    if len(args) <= 0:
        bot.send_message(
            chat_id = update.message.chat_id,
            text="Falta de argumentos."
        )
        return

    prob_actions = []
    isSentence = False

    for word in args:
        if word[0] == '\"':
            isSentence = True
            word = word[1:]

            auxSentence = word + " "

        elif word[-1] == '\"' :
            isSentence = False
            word = word[:-1]

            prob_actions.append(auxSentence+word)

        elif isSentence == True:
            auxSentence = auxSentence + word + " "

        else:
            prob_actions.append(word)

    value = randint(0, 100)
    value %= len(prob_actions)

    bot.send_message(
        chat_id=update.message.chat_id,
        text="A decisão mais sábia parece ser: "+prob_actions[value]
    )

def randomgifidol(bot, update, args):
    if len(args) <= 0: thereisidol = False

    else:
        idol = args[0].lower()

        thereisidol = True

        value = randint(0, 100)
        value %= 3

        if idol == "seulgi":        gif2send = SEULGI_GIFS[value]
        elif idol == "dahyun":      gif2send = DAHYUN_GIFS[value]
        elif idol == "nayeon":      gif2send = NAYEON_GIFS[value]
        elif idol == "sana":        gif2send = SANA_GIFS[value]
        elif idol == "jihyo":       gif2send = JIHYO_GIFS[value]
        elif idol == "moonbyul":    gif2send = MOONBYUL_GIFS[value]
        else:                       thereisidol = False

    if thereisidol == True :
        bot.sendAnimation(
            chat_id = update.message.chat_id,
            animation=gif2send
        )
    else:
        bot.send_message(
            chat_id = update.message.chat_id,
            text=("Desculpe. Não entendi. Temos gifs das idols:\n"+
            "/idol Nayeon\n"+"/idol Seulgi\n"+"/idol Sana\n"+"/idol Dahyun\n"+
            "/idol Jihyo\n"+"/idol Moonbyul")
        )

def mydispatcher(disp):
    disp.add_handler(CommandHandler('start', start))
    disp.add_handler(CommandHandler('http', http_cats, pass_args=True))
    disp.add_handler(CommandHandler('who', who))
    disp.add_handler(CommandHandler('help', help))
    disp.add_handler(CommandHandler('about', about))
    disp.add_handler(CommandHandler('idol', randomgifidol, pass_args=True))
    disp.add_handler(CommandHandler('decision', undecided, pass_args=True))

    disp.add_handler(MessageHandler(Filters.text, rtext))

    #disp.add_handler(CommandHandler('undecided', undecided, pass_args=True))

    #command don't expected
    disp.add_handler(MessageHandler(Filters.command, unknown))

    disp.add_handler(MessageHandler(Filters.audio | Filters.voice, raudio))
    disp.add_handler(MessageHandler(Filters.animation | Filters.video, ranimation))
