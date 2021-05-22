from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Question(models.Model):
    question_text = models.CharField(max_length=200,verbose_name="投票问题描述")
    pub_date = models.DateTimeField(verbose_name="发布时间")

    class Meta:
        verbose_name_plural='投票问题'
        verbose_name="投票问题描述"

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse('polls:index')



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,verbose_name="投票问题")
    choice_text = models.CharField(max_length=200,verbose_name="投票选项描述")
    votes = models.IntegerField(default=0,verbose_name='票数')
    voted_users = models.ManyToManyField(User, through='UserVote')

    class Meta:
        verbose_name_plural='投票选项'
        verbose_name="投票选项"

    def __str__(self):
        return self.choice_text

    def get_absolute_url(self):
        return reverse('polls:listchoice')


class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    vote_datetime = models.DateTimeField(auto_now_add=True)
