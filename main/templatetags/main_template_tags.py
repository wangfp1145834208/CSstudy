#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/9/27

from django import template

from ..models import Category

register = template.Library()


@register.inclusion_tag('cats.html')
def get_category_list(app_name):
    print('app_name =', app_name)
    cat_list = Category.objects.all()
    if app_name == 'article':
        cat_list = (cat for cat in cat_list if cat.post_set.count() > 0)
        url_name = 'article:cat_post'
    elif app_name == 'collection':
        cat_list = (cat for cat in cat_list if cat.website_set.count() > 0)
        url_name = 'collection:cat_web'
    else:
        raise ValueError(r"'app_name' must be 'article' or 'collection'!")
    return {'cat_list': cat_list, 'url_name': url_name}

# 注意两点：
# 1.自定义tag的参数可以通过模板中的变量传入，也可以通过字符串（即外带引号）传入
# 2.在模板中'{% %}'内的变量不需要'{{ }}'
