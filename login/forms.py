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
    age=forms.ChoiceField(label="是否适龄", choices=[(0, u'否'),(1, u'是')], initial ='',widget=forms.Select(),required=True)
    credit=forms.ChoiceField(label="个人信用", choices=[(3,u'好'),(2,u'信用一般'),(3,u'信用差')], initial ='',widget=forms.Select(),required=True)
    guarantee=forms.ChoiceField(label="有无担保",choices=[(1,u'有担保'),(0, '无担保')], initial ='',widget=forms.Select(),required=True)
    income=forms.ChoiceField(label="收入水平", choices=[(1,u'收入低'),(2, u'一般'),(3, u'中'),(4, u'高')], initial ='',widget=forms.Select(),required=True)
    house=forms.ChoiceField(label="有无房产",choices=[(1, u'有'),(0,u'无')], initial ='',widget=forms.Select(),required=True)

