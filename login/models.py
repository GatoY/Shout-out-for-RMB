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
    age=models.PositiveSmallIntegerField()
    credit=models.PositiveSmallIntegerField()
    vouch=models.PositiveSmallIntegerField()
    income=models.PositiveSmallIntegerField()
    house=models.PositiveSmallIntegerField()
    decision=models.PositiveSmallIntegerField()
    def __str__(self):
        return "loanform"
# Create your models here.
