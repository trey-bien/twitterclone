from django.db import models
from tweet.models import Tweet
from twitteruser.models import MyUser

class Notification(models.Model):
    notified_user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)