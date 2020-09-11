import telebot
from .models import QuestionSet, Config, TelegramUser, BroadcastMessage
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from .TOKENS import token
bot = telebot.TeleBot(token, parse_mode=None)

empty_markup = telebot.types.ReplyKeyboardRemove(selective=False)


def get_question_list():
    return QuestionSet.objects.filter(active=True)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    TelegramUser.objects.get_or_create(chat_id=message.chat.id)
    model = Config.objects.filter(name="start_msg").last()
    text = ''
    if model:
        text = model.value
    else:
        text = 'سلام به بات فارابی خوش آمدی. میتونی با کمک دستور /questions لیست سوالات رو مشاهده کنی.'
    bot.reply_to(message, text, reply_markup=empty_markup)


@bot.message_handler(commands=['help'])
def send_help(message):
    model = Config.objects.filter(name="help_msg").last()
    text = ''
    if model:
        text = model.value
    else:
        text = 'سلام به بات فارابی خوش آمدی. میتونی با کمک دستور /questions لیست سوالات رو مشاهده کنی.'
    bot.reply_to(message, text, reply_markup=empty_markup)


@bot.message_handler(commands=['questions'])
def send_welcome(message):
    questions = get_question_list()
    

    if questions.count() == 0:
        bot.reply_to(message, 'سوالی وجود ندارد.')
    
    else:

        text = ''
        markup = telebot.types.ReplyKeyboardMarkup()

        for index, question in enumerate(questions):
            text += str(index+1) + '.' + question.question + '\n'
            itembtna = telebot.types.KeyboardButton(str(index+1))
            markup.add(itembtna)

        msg = bot.send_message(message.chat.id, text, reply_markup=markup)
        bot.register_next_step_handler(msg, get_question)


def get_question(message):
    
    text = message.text

    if not text.isdigit():
        bot.reply_to(message, 'این سوال وجود ندارد.', reply_markup=empty_markup)
    else:
        number = int(text)
        questions = get_question_list()
        if questions.count() >= number:
            question = questions[number-1]
            question.access_count = question.access_count + 1
            question.save()
            bot.reply_to(message, question.answer, reply_markup=empty_markup)
        else:
            bot.reply_to(message, 'این سوال وجود ندارد.', reply_markup=empty_markup)



@receiver(post_save, sender=BroadcastMessage)
def broadcast_message(sender, instance, **kwargs):
    text = instance.text
    users = TelegramUser.objects.all()
    for user in users:
        try:
            msg = bot.send_message(user.chat_id, text, reply_markup=empty_markup)
        except:
            pass


def start_polling():
    print('TELEGRAM BOT STARTED ...')
    bot.polling()
