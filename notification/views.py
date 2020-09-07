from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from twitteruser.models import MyUser
from tweet.models import Tweet
from notification.models import Notification


@login_required
def notification_view(request):
    new_notifications = []
    notifications = Notification.objects.filter(notified_user=request.user)
    for notification in notifications:
        if notification.viewed == False:
            new_notifications.append(notification)
            notification.viewed = True
            notification.save()
            
    return render(request, 'notification.html', {"new_notifications": new_notifications})


