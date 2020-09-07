from django.db import models
from twitteruser.models import MyUser
from django.utils import timezone

class Tweet(models.Model):
    body = models.CharField(max_length=140)
    tweeter = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body
    
