from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import datetime, timedelta


class TodoItem(models.Model):
    Important = 0
    MVP_Project = 1
    Compound_Effect = 2
    General = 3
    Sub_General = 4
    Emergence_Today =  5
    Emergence_Week = 6
    Emergece_Month = 7
    Aim_Today =  8
    Aim_Week= 9
    Aim_Month = 10
    THE_ONE_THING  = 11
    TECH =  12
    Remind =  13
    Priorities = (
                (Important,'重要事項(優先處理)'),
                (MVP_Project,'手頭最重要的項目(當紅炸子雞項目)'),
                (Compound_Effect,'每天都堅持要做的事情(風雨無阻)'),
                (General,'一般'),
                (Sub_General,'準一般'),
                (Emergence_Today,'今日緊急項目'),
                (Emergence_Week,'本周緊急項目'),
                (Emergece_Month,'本月緊急'),
                (Aim_Today,'今日目標'),
                (Aim_Week,'本周目標'),
                (Aim_Month,'本月目標'),
                (THE_ONE_THING,'唯一重要的事情'),
                (TECH,'技術盞'),
                (Remind,'提醒'),)
    content =models.TextField(default='今天目標是:')
    deadline = models.PositiveIntegerField(default=0,null=True)
    rating = models.IntegerField(
            choices=Priorities,
            default=0,
            null=True)
    hours = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    create_time=models.DateTimeField(auto_now_add=True)
    last_edit=models.DateTimeField(auto_now=True)
    class Meta:
            ordering = ('create_time','last_edit','rating','content',)
    def __str__(self):
        return f'{self.content} ({self.hours})'
    def get_absolute_url(self):
        return reverse('todo')

class BinItem(models.Model):
    content =models.TextField()
    delete_time=models.DateTimeField()
    def __str__(self):
        return self.content

class DoneItem(models.Model):
    content =models.TextField()
    done_time=models.DateTimeField()
    def __str__(self):
        return self.content


