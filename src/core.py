# Main code
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
