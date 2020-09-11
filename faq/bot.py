import telebot
from .models import QuestionSet, Config, TelegramUser, BroadcastMessage
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from .TOKENS import token
bot = telebot.TeleBot(token, parse_mode=None)

empty_markup = telebot.types.ReplyKeyboardRemove(selective=False)


def get_question_list():
    return QuestionSet.objects.filter(active=True).order_by('rank')


def get_config_text(name, default):
    model = Config.objects.filter(name=name).last()
    text = ''
    if model:
        text = model.value
    else:
        text = default
    return text



@bot.message_handler(commands=['start'])
def send_welcome(message):
    TelegramUser.objects.get_or_create(chat_id=message.chat.id)
    text = get_config_text('start_msg', 'سلام به بات فارابی خوش آمدی. میتونی با کمک دستور /questions لیست سوالات رو مشاهده کنی.')
    bot.reply_to(message, text, reply_markup=empty_markup)


@bot.message_handler(commands=['help'])
def send_help(message):
    text = get_config_text('help_msg', 'سلام به بات فارابی خوش آمدی. میتونی با کمک دستور /questions لیست سوالات رو مشاهده کنی.')
    bot.reply_to(message, text, reply_markup=empty_markup)


@bot.message_handler(commands=['questions'])
def send_questions(message):
    questions = get_question_list()
    

    text = get_config_text('empty_questions', 'سوالی وجود ندارد.')
    if questions.count() == 0:
        bot.reply_to(message, )
    
    else:

        text = ''
        markup = telebot.types.ReplyKeyboardMarkup(row_width=3)

        buttons = []

        tmp_buttons = []
        for index, question in enumerate(questions):
            text += str(index+1) + '.' + question.question + '\n'
            tmp_buttons.append(telebot.types.KeyboardButton(str(index+1)))
            if index % 4 == 3 or index == questions.count()-1:
                markup.add(*tmp_buttons)
                tmp_buttons = []

        msg = bot.send_message(message.chat.id, text, reply_markup=markup)
        bot.register_next_step_handler(msg, get_question)


def get_question(message):
    
    text = message.text

    if not text.isdigit():
        text = get_config_text('not_valid_question', 'این سوال وجود ندارد.')
        bot.reply_to(message, text, reply_markup=empty_markup)
    else:
        number = int(text)
        questions = get_question_list()
        if questions.count() >= number:
            question = questions[number-1]
            question.access_count = question.access_count + 1
            question.save()
            bot.reply_to(message, question.answer, reply_markup=empty_markup)
        else:
            text = get_config_text('not_valid_question', 'این سوال وجود ندارد.')
            bot.reply_to(message, text, reply_markup=empty_markup)



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
