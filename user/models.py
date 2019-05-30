from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    mobile=models.CharField('手机号码',max_length=11,unique=True)
    qq = models.CharField('QQ', max_length=20, unique=True)
    wx = models.CharField('微信', max_length=20, unique=True)

    def __str__(self):
        return self.username