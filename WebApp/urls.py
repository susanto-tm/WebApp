"""WebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from WebApp import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

import WebApp.forms

urlpatterns = [
    # url(r'^admin/', include(admin.sites.url)),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^login/$', 
        auth_views.login,
        {
            'template_name': 'WebApp/login.html',
            'authentication_form': WebApp.forms.LoginFields,
            'extra_context':
            {
                'title': 'Login Page',
            },
        },
        name='login'),
    url(r'^logout/$',
        auth_views.logout,
        {
            'next_page': '/', 
        },
        name='logout'),
    # path('', views.home, name='home'),
]
urlpatterns += staticfiles_urlpatterns()

