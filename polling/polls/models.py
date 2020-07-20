from django.conf import settings
from django.db import models


# Create your models here.


class Polls(models.Model):
    UniqueId = models.CharField(max_length=100, unique=True)
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    Active = models.BooleanField(default=True)
    Author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class UserModel(models.Model):
    Name = models.CharField(max_length=100)
    CurrentPoll = models.ForeignKey(
        Polls, on_delete=models.CASCADE)


class Question(models.Model):
    QuestionText = models.CharField(max_length=100)
    Upvotes = models.IntegerField()
    Downvotes = models.IntegerField()
    User = models.ForeignKey(
        UserModel, on_delete=models.CASCADE)
