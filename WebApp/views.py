"""
Definitions of Views
"""

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def home(request):
    """Renders the home page."""
    return render(
        request,
        'WebApp/base.html',
        {
            'title': 'Home',
        }
    )

