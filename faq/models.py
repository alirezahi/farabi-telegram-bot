from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionSet(models.Model):
    question = models.TextField(verbose_name='سوال')
    answer = models.TextField(verbose_name='پاسخ')
    active = models.BooleanField(default=True, verbose_name='فعال')
    rank = models.IntegerField(null=True, blank=True, verbose_name='رتبه')
    access_count = models.IntegerField(default=0, verbose_name='مقدار استفاده')

    class Meta:
        verbose_name = 'مجموعه سوالات'

class Config(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    value = models.TextField(verbose_name='مقدار')

    class Meta:
        verbose_name = 'تنظیمات'


class TelegramUser(User):
    chat_id = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'کاربران'


class BroadcastMessage(models.Model):
    text = models.TextField(verbose_name='متن پیام')

    class Meta:
        verbose_name = 'ارسال همگانی پیام'

