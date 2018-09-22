"""
Definitions of Views
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView, CreateView
from WebApp.forms import HomeForms, SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = "WebApp/index.html"

    def get(self, request):
        form = HomeForms
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'title': 'Home',
            }
        )


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
    return render(request, 'WebApp/signup.html', {'form': form})


