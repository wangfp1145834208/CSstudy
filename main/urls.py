#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/9/25

from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.to_index),
    url(r'^index/$', views.index, name='index'),
    url(r'^add_category/$', views.add_category, name='add_category'),
]
