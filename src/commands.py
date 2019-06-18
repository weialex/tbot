# When user send a command
from telegram import InlineKeyboardMarkup
from random import seed, randint

from conf.inline_menus import *
from conf.texts4messages import *
from conf.settings import HTTP_CATS_URL

def start(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text=START_WELCOME
    )

def about(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text=ABOUT_MESSAGE
    )

def help(bot, update, args):
    if len(args) != 1:
        bot.send_message(
            chat_id = update.message.chat_id,
            text=HELP_DEFAULT
        )
        return

    command = args[0].lower()

    if command == "http": text = HELP_HTTP
    elif command == "decision": text = HELP_DECISION

def motivacional(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text=HELP_MESSAGE
    )
    bot.sendPhoto(
        chat_id = update.message.chat_id,
        photo = "https://p2.trrsf.com/image/fget/cf/940/0/images.terra.com/2018/07/19/pudim-de-geladeira.jpg"
    )

def undecided(bot, update, args):
    if len(args) <= 0:
        bot.send_message(
            chat_id = update.message.chat_id,
            text=MISS_ARG_MSG
        )
        return

    prob_actions = []
    isSentence = False

    for word in args:
        if word[0] == '\"':
            if word[-1] != '\"':
                isSentence = True
                word = word[1:]
                auxSentence = word + " "
            else: prob_actions.append(word[1:-1])

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

def idol(bot, update):
    reply_markup = InlineKeyboardMarkup(idol_list)

    bot.send_message(
        chat_id = update.message.chat_id,
        text="Escolha a idol que quer receber um gif",
        reply_markup=reply_markup
    )

def sendIdolGif(bot, update, query):
    value = randint(0, 100)
    value %= 3
    index_idol=query.data

    if index_idol == '1': gif2send, chosenidol = NAYEON_GIFS[value], "Nayeon"
    elif index_idol == '2': gif2send, chosenidol = SEULGI_GIFS[value], "Seulgi"
    elif index_idol == '3': gif2send, chosenidol = SANA_GIFS[value], "Sana"
    elif index_idol == '4': gif2send, chosenidol = DAHYUN_GIFS[value], "Dahyun"
    elif index_idol == '5': gif2send, chosenidol = JIHYO_GIFS[value], "Jihyo"
    elif index_idol == '6': gif2send, chosenidol = MOONBYUL_GIFS[value], "Moonbyul"

    bot.sendAnimation(
        chat_id=query.message.chat_id,
        animation=gif2send
    )
    chosenidol = "Idol: "+chosenidol

    return chosenidol

def get_url():
    #contents = requests.get('http://www.pudim.com.br').json()
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def teste(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def http_cats(bot, update, args):
    bot.sendPhoto(
        chat_id = update.message.chat_id,
        photo = HTTP_CATS_URL + args[0]
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
