# -*- coding:utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(u'标题',max_length=30)
    text = models.TextField(u'内容')
    created_date = models.DateTimeField(u'创建日期',default=timezone.now)
    published_date = models.DateTimeField(u'出版日期',blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

