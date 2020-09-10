import telebot
from .models import QuestionSet

from .TOKENS import token
bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "سلام به بات فارابی خوش آمدی. میتونی با کمک دستور \questions لیست سوالات رو مشاهده کنی.")


@bot.message_handler(commands=['questions'])
def send_welcome(message):
    questions = QuestionSet.objects.filter(active=True)
    text = ''
    for index, question in enumerate(questions):
        text += str(index) + '.' + question.question + '\n'
	bot.reply_to(message, "text")

def start_polling():
    try:
        bot.polling()
    except error as err:
        print(st(err))
    print('TELEGRAM BOT STARTED ...')