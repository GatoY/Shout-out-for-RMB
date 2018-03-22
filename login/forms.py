# -*- coding:utf-8 -*-
from django.contrib.auth.forms import UserCreationForm, forms
from .models import User
from django import forms

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username",)
#review
class inForm(forms.Form):
    age = forms.IntegerField(label='是否适龄')
    credit=forms.IntegerField(label="信用评分")
    guarantee=forms.IntegerField(label="有无担保")
    income=forms.IntegerField(label="收入水平")
    house=forms.IntegerField(label="有无房产")

