#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/9/26

from django import forms
from django.contrib.auth.forms import \
    (UserCreationForm, AuthenticationForm, PasswordChangeForm)
from django.contrib.auth import password_validation

from .models import UserProfile


class UserForm(UserCreationForm):
    error_messages = {
        'password_mismatch': '两次输入的密码不相同。',
    }
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label='用户名', help_text="只能包含字母，数字及‘@’、‘.’、‘+’、‘-’、‘_’符号，用户名中不能包含空格")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             label='邮箱地址', required=False, help_text='(选填)')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                label='密码', strip=False,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                label='确认密码', strip=False,
                                help_text='请确保与上次输入的密码一致')

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label='用户名')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               label='密码', strip=False)


class PassChangeForm(PasswordChangeForm):
    error_messages = {
        'password_mismatch': "两次输入的密码不相同。",
        'password_incorrect': "旧密码输入错，请再次输入。"
    }
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                   label='旧密码', strip=False)
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                    label='新密码', strip=False,
                                    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                    label='确认密码', strip=False,
                                    help_text='请确保与上次输入的密码一致')


class UserProfileForm(forms.ModelForm):  # TODO
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                label='姓', required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                 label='名', required=False)
    nickname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label='昵称', required=False)
    birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                            label='出生日期')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             label='邮箱地址', required=False)
    signature = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
                                label='签名', required=False)

    class Meta:
        model = UserProfile
        fields = ('last_name', 'first_name', 'birth', 'nickname', 'email', 'signature')
