# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        pass

@python_2_unicode_compatible
class LoanForm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age=models.IntegerField(u'是否适龄',choices=[(0, u'否'),(1, u'是')],default=u'否')
    credit=models.IntegerField(u'信用情况', choices=[(3,u'好'),(2,u'信用一般'),(3,u'信用差')],default=1)
    vouch=models.IntegerField(u'有无担保', choices=[(1,u'有担保'),(0, '无担保')],default=1)
    income=models.IntegerField(u'收入水平', choices=[(1, u'低'),(2, u'一般'),(3, u'中'),(4, u'高')],default=1)
    house=models.IntegerField(u'有无房产',choices=[(1, u'有'),(0,u'无')],default=1)
    decision=models.BooleanField()
    def __str__(self):
        return "loanform"
# Create your models here.
