from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        pass

@python_2_unicode_compatible
class loanForm(models.Model):
    age=models.BooleanField(default=False)
    credit=models.PositiveSmallIntegerField()
    vouch=models.BooleanField(default=False)
    income=models.PositiveSmallIntegerField()
    house=models.BooleanField(default=False)
    decision=models.BooleanField(default=False)
    def __str__(self):
        return null
# Create your models here.
