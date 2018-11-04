"""
Definitions of Views
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView, CreateView
from WebApp.forms import SignUpForm, LoginFields
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
import pyrebase

config = {
    'apiKey': "AIzaSyBwZ-lzqDRd19r26J7wzn-IsC6JuHtn6vU",
    'authDomain': "cas-webdevelopment.firebaseapp.com",
    'databaseURL': "https://cas-webdevelopment.firebaseio.com",
    'projectId': "cas-webdevelopment",
    'storageBucket': "cas-webdevelopment.appspot.com",
    'messagingSenderId': "481704047225"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


class HomeView(TemplateView):
    template_name = 'WebApp/home.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                'title': 'Home',
            }
        )


# def login_view(request):
#     if request.method == "POST":
#         form = LoginFields(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('username')
#             passw = form.cleaned_data.get('password')
#             user = auth.sign_in_with_email_and_password(email, passw)
#             return redirect('home')
#     else:
#         form = LoginFields()
#     return render(request, 'WebApp/login2.html', {'form': form})
#

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'WebApp/signup2.html', {'form': form})
