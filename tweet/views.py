from django.shortcuts import render, HttpResponseRedirect, reverse

from tweet.forms import NewTweetForm
from tweet.models import Tweet
from twitteruser.models import MyUser
from notification.models import Notification

import re

def new_tweet_view(request):
    if request.method == "POST":
        form = NewTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user_mention = re.findall(r'@([\w]+)', data.get("body"))
            new_tweet = Tweet.objects.create(
                body = data.get('body'),
                tweeter = request.user
            )
            if user_mention:
                for mention in user_mention:
                    Notification.objects.create(
                        tweet = new_tweet,
                        notified_user = MyUser.objects.get(username=mention),
                    )
            return HttpResponseRedirect(reverse("homepage"))

    form = NewTweetForm()
    return render(request, "new_tweet.html", {"form": form})

def tweet_detail_view(request, tweet_id):
    tweet = Tweet.objects.filter(id=tweet_id).first()
    return render(request, "tweet_detail.html", {"tweet":tweet})