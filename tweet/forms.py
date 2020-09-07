from django import forms
from tweet.models import Tweet

class NewTweetForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)



# body = models.CharField(max_length=140)
# tweeter = models.ForeignKey(MyUser, on_delete=models.CASCADE)
# date_time = models.DateTimeField(default=timezone.now)