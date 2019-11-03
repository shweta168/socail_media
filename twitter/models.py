from django.db import models
# from __future__ import unicode_literals
from django.contrib.auth.models import User
# Create your models here.
class TwitterCredentials(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=100,null=True)
    access_secret = models.CharField(max_length=100,null=True)
    consumer_key = models.CharField(max_length=100,null=True)
    consumer_secret = models.CharField(max_length=100,null=True)
# Create your models here.
