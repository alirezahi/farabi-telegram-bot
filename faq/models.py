from django.db import models

# Create your models here.


class QuestionSet(models.Model):
    question = models.TextField()
    answer = models.TextField()
    active = models.BooleanField(default=True)
    rank = models.IntegerField(null=True, blank=True)

class Config(models.Model):
    name = models.CharField(max_length=100)
    value = models.TextField()