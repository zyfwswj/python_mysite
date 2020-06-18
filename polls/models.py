import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
  question_text = models.CharField('题干', max_length=200)
  pub_date = models.DateTimeField('发布时间')

  def __str__(self):
    return self.question_text

  def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField('选项', max_length=200)
  votes = models.IntegerField('支持人数', default=0)

  def __str__(self):
    return self.choice_text
