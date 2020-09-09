from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from authentication.forms import LoginForm

# def login_view(request):
# 	if request.method == "POST":
# 		form = LoginForm(request.POST)
# 		if form.is_valid():
# 			data = form.cleaned_data
# 			user = authenticate(request, username=data.get("username"), password=data.get("password"))
# 			if user:
# 				login(request, user)
# 				return HttpResponseRedirect(reverse("homepage"))
	
# 	form = LoginForm()
# 	return render(request, "login_form.html", {"form":form})

class LoginView(TemplateView):

	def get(self, request):
		form = LoginForm()
		return render(request, "login_form.html", {"form":form})

	def post(self, request):
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = authenticate(request, username=data.get("username"), password=data.get("password"))
			if user:
				login(request, user)
				return HttpResponseRedirect(reverse("homepage"))
		else:
			return render(request, "login_form.html", {"form":form})

# def logout_view(request):
# 	logout(request)
# 	return HttpResponseRedirect(reverse("homepage"))

class LogoutView(TemplateView):
	
	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse("homepage"))

