#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/9/26

from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           max_length=128, label='分类名称', help_text='请以大写字母开头',
                           error_messages={'unique': '该分类已经存在'})
    describe = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
                               max_length=300, label='分类描述', help_text='（可选内容）', required=False)
    slug = forms.CharField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Category
        fields = ('name', 'describe', 'slug')
