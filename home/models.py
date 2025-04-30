# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Job Seeker(models.Model):

    #__Job Seeker_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    experience = models.CharField(max_length=255, null=True, blank=True)
    phone number = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Job Seeker_FIELDS__END

    class Meta:
        verbose_name        = _("Job Seeker")
        verbose_name_plural = _("Job Seeker")


class Job Provider(models.Model):

    #__Job Provider_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    job title = models.TextField(max_length=255, null=True, blank=True)
    salary = models.TextField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Job Provider_FIELDS__END

    class Meta:
        verbose_name        = _("Job Provider")
        verbose_name_plural = _("Job Provider")



#__MODELS__END
