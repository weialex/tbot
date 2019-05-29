from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import TELEGRAM_TOKEN, HTTP_CATS_URL

def start(bot, update):
    response_message = "Bem vindo ao bot Talklicious."##+'\n'+""
    bot.send_message(
        chat_id = update.message.chat_id,
        text=response_message
    )

def http_cats(bot, update, args):
    bot.sendPhoto(
        chat_id = update.message.chat_id,
        photo = HTTP_CATS_URL + args[0]
    )

def help(bot, update):
    response_message = "Desculpa não ajudar, nem mesmo eu sei o que estou fazendo."+'\n'+"Mas para te animar, segue esse belo pudim."
    bot.send_message(
        chat_id = update.message.chat_id,
        text=response_message
    )
    bot.sendPhoto(
        chat_id = update.message.chat_id,
        photo = "https://p2.trrsf.com/image/fget/cf/940/0/images.terra.com/2018/07/19/pudim-de-geladeira.jpg"
    )

def about(bot, update):
    response_message = "Apenas para exercício do aprendizado de chatbot. Feito com a ajuda de: https://github.com/mdcg/http-cats-telegram-bot"
    bot.send_message(
        chat_id = update.message.chat_id,
        text=response_message
    )    
 
def unknown(bot, update):
    response_message = "Comando inexistente."
    bot.send_message(
        chat_id = update.message.chat_id,
        text=response_message
    )

def main():
    updater = Updater(token = TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )

    dispatcher.add_handler(
        CommandHandler('http', http_cats, pass_args=True)
    ) #arg eh o argumento que vem junto do comando no telegram /command arg

    dispatcher.add_handler(
        CommandHandler('help', help)
    )

    dispatcher.add_handler(
        CommandHandler('about', about)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    ) #no caso do cliente enviar algo diferente de um dos comandos
      #atribuidos acima, cai em unknown()

    updater.start_polling() #busca atualizacoes do telegram ao chatbot
    updater.idle() #bloqueia ate receber um sinal e pare o updater

if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()
