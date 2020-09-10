import telebot

from .TOKENS import token
bot = telebot.TeleBot("TOKEN", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


def start_polling():
    print('TELEGRAM BOT STARTED ...')
    bot.polling()