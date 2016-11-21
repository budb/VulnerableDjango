"""Vulnerable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

from Vulnerable.views import stage_1, stage_2, stage_3, stage_4

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots.txt$', RedirectView.as_view(url='https://www.youtube.com/watch?v=oHg5SJYRHA0')),
    url(r'^$', stage_1),
    url(r'^stage_1/$', stage_1),
    url(r'^stage_2/$', stage_2),
    url(r'^stage_3/$', stage_3),
    url(r'^stage_4/$', stage_4),
    
]
