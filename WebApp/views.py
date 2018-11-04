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
