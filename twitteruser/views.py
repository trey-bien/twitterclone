from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from twitteruser.models import MyUser
from twitteruser.forms import SignupForm
from tweet.models import Tweet
from notification.models import Notification

@login_required
def index_view(request):
    user_tweets = Tweet.objects.filter(tweeter=request.user).order_by("-date_time")
    followee_tweets = Tweet.objects.filter(tweeter__in=request.user.follow.all()).order_by("-date_time")
    all_tweets = user_tweets | followee_tweets
        
    return render(request, "index.html", {"user_tweets": user_tweets, "followwee_tweets": followee_tweets, "all_tweets": all_tweets})

# def signup_view(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             new_user = MyUser.objects.create_user(
#                 username = data.get("username"),
#                 password = data.get("password"),
#             )
#             login(request, new_user)
#             return HttpResponseRedirect(reverse("homepage"))
#     form = SignupForm()
#     return render(request, "signup_form.html", {"form": form})

class SignupView(TemplateView):

    def get(self, request):
        form = SignupForm()
        return render(request, "signup_form.html", {"form": form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(
                username = data.get("username"),
                password = data.get("password"),
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))
        else:
            return render(request, "signup_form.html", {"form": form})


# def user_detail_view(request, user_id):
#     user_profile = MyUser.objects.get(id=user_id)
#     user_tweets = Tweet.objects.filter(tweeter=user_profile).order_by("-date_time")
#     tweet_count = len(user_tweets)
#     following_list = list(user_profile.follow.all())
#     following_count = len(following_list)
#     return render(request, "user_detail.html", {"user_profile": user_profile, "user_tweets": user_tweets, "tweet_count": tweet_count, "following_list": following_list, "following_count": following_count})

class UserDetailView(TemplateView):
    
    def get(self, request, user_id):
        user_profile = MyUser.objects.get(id=user_id)
        user_tweets = Tweet.objects.filter(tweeter=user_profile).order_by("-date_time")
        tweet_count = len(user_tweets)
        following_list = list(user_profile.follow.all())
        following_count = len(following_list)
        return render(request, "user_detail.html", {"user_profile": user_profile, "user_tweets": user_tweets, "tweet_count": tweet_count, "following_list": following_list, "following_count": following_count})

@login_required
def follow_view(request, user_id):
    followee = MyUser.objects.filter(id=user_id).first()
    request.user.follow.add(followee)
    return HttpResponseRedirect(reverse("homepage"))

@login_required
def unfollow_view(request, user_id):
    followee = MyUser.objects.filter(id=user_id).first()
    request.user.follow.remove(followee)
    return HttpResponseRedirect(reverse("homepage"))