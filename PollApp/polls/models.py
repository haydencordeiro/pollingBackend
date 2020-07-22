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

    def __str__(self):
        return str(self.Title)


class UserModel(models.Model):
    Ip = models.CharField(max_length=100, null=True)
    Name = models.CharField(max_length=100)
    CurrentPoll = models.ForeignKey(
        Polls, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Question(models.Model):
    poll = models.ForeignKey(
        Polls, on_delete=models.CASCADE, null=True)
    QuestionText = models.CharField(max_length=100)
    Completed = models.BooleanField(default=False)
    User = models.ForeignKey(
        UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.QuestionText


class UpvoteLogs(models.Model):
    Question = models.ForeignKey(
        Question, on_delete=models.CASCADE)
    UserFK = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, null=True)


class DownvoteLogs(models.Model):
    Question = models.ForeignKey(
        Question, on_delete=models.CASCADE)
    UserFK = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, null=True)
