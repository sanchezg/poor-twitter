from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Tweet(models.Model):
    """Simple model to represent a tweet in DataBase."""
    text = models.TextField(max_length=settings.MAX_TWEET_LENGTH)  # Tweet text
    date_time = models.DateTimeField(auto_now_add=True)  # Tweet creation datetime
    username = models.CharField(max_length=settings.MAX_USERNAME_LENGTH)  # Tweet user
