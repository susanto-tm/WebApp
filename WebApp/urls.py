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
from django.urls import path
from WebApp import views, forms
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^$', views.index_home, name='home'),
    url(r'^login/$',
        auth_views.LoginView.as_view(template_name='WebApp/login2.html'),
        {
            'authentication_form': forms.LoginFields,
            'extra_context':
            {
                'title': 'Login Page',
            },
        },
        name='login'),
    url(r'^logout/$',
        auth_views.LogoutView.as_view(),
        {
            'next_page': 'home',
        },
        name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    # url(r'^signup-auth/$', views.signup, name='signup-auth'),
    path('forum/', include('forum.urls')),
]
urlpatterns += staticfiles_urlpatterns()

