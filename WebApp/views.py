"""
Definitions of Views
"""

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from WebApp.forms import HomeForms


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