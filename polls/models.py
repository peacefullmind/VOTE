from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Question(models.Model):
    question_text = models.CharField(max_length=200,help_text="投票问题描述")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200,help_text="投票选项描述")
    votes = models.IntegerField(default=0)
    voted_users = models.ManyToManyField(User, through='UserVote')

    def __str__(self):
        return self.choice_text


class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    vote_datetime = models.DateTimeField(auto_now_add=True)
