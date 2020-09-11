from django.db import models

# Create your models here.


class QuestionSet(models.Model):
    question = models.TextField(verbose_name='سوال')
    answer = models.TextField(verbose_name='پاسخ')
    active = models.BooleanField(default=True, verbose_name='فعال')
    rank = models.IntegerField(null=True, blank=True, verbose_name='رتبه')

class Config(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    value = models.TextField(verbose_name='مقدار')