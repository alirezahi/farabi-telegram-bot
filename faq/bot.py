import telebot
from .models import QuestionSet, Config

from .TOKENS import token
bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    model = Config.objects.filter(name="start_msg").last()
    text = ''
    if model:
        text = model.value
    else:
        text = 'سلام به بات فارابی خوش آمدی. میتونی با کمک دستور /questions لیست سوالات رو مشاهده کنی.'
    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def send_help(message):
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
    
    else:

        text = ''
        markup = telebot.types.ReplyKeyboardMarkup()

        for index, question in enumerate(questions):
            text += str(index+1) + '.' + question.question + '\n'
            itembtna = telebot.types.KeyboardButton(str(index+1))

        bot.reply_to(message, text, reply_markup=markup)


def start_polling():
    print('TELEGRAM BOT STARTED ...')
    bot.polling()