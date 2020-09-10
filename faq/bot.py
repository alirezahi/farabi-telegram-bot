import telebot
from .models import QuestionSet, Config

from .TOKENS import token
bot = telebot.TeleBot(token, parse_mode=None)

def return_on_failure(value):
  def decorate(f):
    def applicator(*args, **kwargs):
      try:
         f(*args,**kwargs)
      except:
         print('Error')

    return applicator

  return decorate

@bot.message_handler(commands=['start'])
@return_on_failure
def send_welcome(message):
    model = Config.objects.filter(name="start_msg").last()
    text = ''
    if model:
        text = model.value
    else:
        text = 'سلام به بات فارابی خوش آمدی. میتونی با کمک دستور /questions لیست سوالات رو مشاهده کنی.'
    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
@return_on_failure
def send_help(message):
    model = Config.objects.filter(name="help_msg").last()
    text = ''
    if model:
        text = model.value
    else:
        text = 'سلام به بات فارابی خوش آمدی. میتونی با کمک دستور /questions لیست سوالات رو مشاهده کنی.'
    bot.reply_to(message, text)


@bot.message_handler(commands=['questions'])
@return_on_failure
def send_welcome(message):
    questions = QuestionSet.objects.filter(active=True)

    if questions.count() == 0:
        bot.reply_to(message, 'سوالی وجود ندارد.')

    text = ''
    for index, question in enumerate(questions):
        text += str(index+1) + '.' + question.question + '\n'
    bot.reply_to(message, text)


def start_polling():
    print('TELEGRAM BOT STARTED ...')
    bot.polling()