import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='Bot.log', level=logging.INFO)

#PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
 #   'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def greet_user(update, context):
    print(update)
    update.message.reply_text('Привет! ✋')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context = True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text,talk_to_me))

    logging.info('Bot Started')
    mybot.start_polling()
    mybot.idle()
if __name__ == "__main__":
    main()