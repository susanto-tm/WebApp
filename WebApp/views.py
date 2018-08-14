"""
Definitions of Views
"""

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Album


def home(request):
    """Renders the home page."""
    # all_album = Album.objects.all()
    """
    context = {
        'all_album': all_album,
    }
    """
    return render(request, 'WebApp/index.html')

