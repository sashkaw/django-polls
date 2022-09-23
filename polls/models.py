from django.db import models
from django.utils import timezone
from django.contrib import admin

import datetime

# Create your models here.

class Question(models.Model):
  def __str__(self):
    return self.question_text

  @admin.display(
    boolean=True,
    ordering="pub_data",
    description="Published recently?",
  )
  def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_data <= now

  question_text = models.CharField(max_length=200)
  pub_data = models.DateTimeField("date published")

class Choice(models.Model):
  def __str__(self):
    return self.choice_text

  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
