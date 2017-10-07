#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/9/25

from django.conf.urls import url

from . import views

app_name = 'article'
urlpatterns = [
    url(r'^$', views.posts, name='posts'),
    url(r'^category/(?P<cat_slug>[\w\-]+)/$', views.cat_post, name='cat_post'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/user/personal/$', views.post_person, name='post_person'),
    url(r'^post/author/(?P<username>[\w\@\.\+\-\_]+)/$', views.post_author, name='post_author'),
    url(r'^post/user/add/$', views.post_add, name='post_add'),
    url(r'^post/user/edit/(?P<pk>[0-9]+)/$', views.post_edit, name='post_edit'),
    url(r'^post/user/delete/(?P<pk>[0-9]+)/$', views.post_delete, name='post_delete'),
    url(r'^post/user/like/$', views.post_like, name='post_like'),
    url(r'^post/user/like_cancel/$', views.post_like_cancel, name='post_like_cancel'),
]
