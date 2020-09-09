"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from twitteruser import views as twitteruser_views
from authentication import views as authentication_views
from tweet import views as tweet_views
from notification import views as notification_views

urlpatterns = [
    path('', twitteruser_views.index_view, name="homepage"),
    path('signup/', twitteruser_views.SignupView.as_view(), name="signup"),
    path('login/', authentication_views.LoginView.as_view()),
    path('logout/', authentication_views.LogoutView.as_view()),
    path('newtweet/', tweet_views.new_tweet_view),
    path('tweet/<int:tweet_id>/', tweet_views.tweet_detail_view), 
    path('user/<int:user_id>/', twitteruser_views.UserDetailView.as_view()),
    path('follow/<int:user_id>/', twitteruser_views.follow_view),
    path('unfollow/<int:user_id>/', twitteruser_views.unfollow_view),
    path('notification/', notification_views.notification_view),
    path('admin/', admin.site.urls),
]
