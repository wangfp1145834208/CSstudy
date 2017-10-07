#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/9/27

from django import forms

from .models import Website
from main.models import Category, Tag


class WebsiteForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='标题')
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}),
                          label='网址(URL)', help_text='请填写完整的网址')
    describe = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
                               label='网站描述', help_text='(可以不填)', required=False)
    category = forms.ModelChoiceField(Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}),
                                      label='类型')
    tag = forms.ModelMultipleChoiceField(Tag.objects.all(),
                                         widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
                                         label='标签', help_text='(可以不选)', required=False)

    class Meta:
        model = Website
        fields = ('title', 'url', 'describe', 'category', 'tag')
