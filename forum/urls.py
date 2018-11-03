from django.conf.urls import url, include
from forum import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

app_name = 'forum'

urlpatterns = [
    url(r'^$', views.index, name='forum-index'),
]
