from django.conf.urls import url, include
from forum import views
from django.views.generic import FormView
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views


app_name = 'forum'

urlpatterns = [
    url(r'^$', views.create_post, name='forum-index'),

]
