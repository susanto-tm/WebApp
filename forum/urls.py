from django.conf.urls import url, include
from forum.views import *
from django.views.generic import FormView
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views


app_name = 'forum'

urlpatterns = [
    # url(r'^$', login_required(CreatePost.as_view()), name='forum-index'),
    url(r'^$', create_post, name='forum-index'),
    # url(r'^post/(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post_forum'),
    # url(r'^post-forum/(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post-forum')
    url(r'^post/(?P<slug>[-\w]+)/$', post_detail, name='forum_post')
]
