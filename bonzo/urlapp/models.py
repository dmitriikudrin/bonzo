from datetime import datetime

from django.db import models


class AbstractURL(models.Model):
    class Meta:
        abstract = True

    origin = models.TextField(verbose_name='original link', blank=False, unique=False)
    short = models.CharField(verbose_name='short link', blank=False, unique=False)
    created_at = models.DateTimeField(verbose_name='created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated', auto_now=True)
    last_used_at = models.DateTimeField(verbose_name='last used', blank=True, null=True)

    def update_last_used_time(self):
        self.last_used_at = datetime.now()


class UnknownUserURL(AbstractURL):
    class Meta:
        verbose_name = u'URL of an unregistered user'
        verbose_name_plural = u'URLs of an unregistered user'

    short = models.CharField(verbose_name='short link', max_length=8, blank=False, unique=False)


class RegisteredUserURL(AbstractURL):
    class Meta:
        verbose_name = u'URL of an registered user'
        verbose_name_plural = u'URLs of an registered user'

    short = models.CharField(verbose_name='short link', max_length=5, blank=False, unique=False)
