import telebot
from .models import QuestionSet

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

@return_on_failure
@bot.message_handler(commands=['start'])
def send_welcome(message):
    model = Config.objects.filter(name="start_msg").last()
    text = ''
    if model:
        text = model.value
    else:
        text = 'سلام به بات فارابی خوش آمدی. میتونی با کمک دستور /questions لیست سوالات رو مشاهده کنی.'
    bot.reply_to(message, text)


@return_on_failure
@bot.message_handler(commands=['help'])
def send_help(message):
    model = Config.objects.filter(name="help_msg").last()
    text = ''
    if model:
        text = model.value
    else:
        text = 'سلام به بات فارابی خوش آمدی. میتونی با کمک دستور /questions لیست سوالات رو مشاهده کنی.'
    bot.reply_to(message, text)


@return_on_failure
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
    print('TELEGRAM BOT STARTED ...')
    bot.polling()