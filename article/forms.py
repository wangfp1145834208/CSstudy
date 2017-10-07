#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/9/26

from django import forms

from .models import Post, Tag
from main.models import Category


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='标题')
    excerpt = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='摘要',
                              required=False, help_text='（可选内容）')
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '40'}), label='文章')
    category = forms.ModelChoiceField(Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}),
                                      label='类型')
    mark_down = forms.BooleanField(label='使用markdown', required=False)

    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'mark_down', 'body', 'category')
