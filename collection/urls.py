#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/9/25

from django.conf.urls import url

from . import views

app_name = 'collection'
urlpatterns = [
    url(r'^websites/$', views.websites, name='websites'),
    url(r'^website/add', views.add_website, name='add_website'),
    url(r'^category/(?P<cat_slug>[\w\-]+)/$', views.cat_web, name='cat_web'),
    url(r'^website/collected/$', views.web_collected, name='web_collected'),
    url(r'^website/collected/cancel/$', views.collected_cancel, name='collected_cancel'),
]
