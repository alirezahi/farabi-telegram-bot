import telebot
from .models import QuestionSet

from .TOKENS import token
bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    model = Config.objects.filter(name="start_msg").last()
    text = ''
    if model:
        text = model.value
    else:
        text = 'سلام به بات فارابی خوش آمدی. میتونی با کمک دستور /questions لیست سوالات رو مشاهده کنی.'
    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    model = Config.objects.filter(name="help_msg").last()
    text = ''
    if model:
        text = model.value
    else:
        text = 'سلام به بات فارابی خوش آمدی. میتونی با کمک دستور /questions لیست سوالات رو مشاهده کنی.'
    bot.reply_to(message, text)


@bot.message_handler(commands=['questions'])
def send_welcome(message):
    questions = QuestionSet.objects.filter(active=True)

    if questions.count() == 0:
        bot.reply_to(message, 'سوالی وجود ندارد.')

    text = ''
    for index, question in enumerate(questions):
        text += str(index+1) + '.' + question.question + '\n'
    bot.reply_to(message, text)


def start_polling():
    while True:
        try:
            bot.polling()
        except Exception as err:
            print(str(err))
        print('TELEGRAM BOT STARTED ...')