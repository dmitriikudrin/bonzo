from datetime import datetime

from django.db import models

from authapp.models import BonzoUser


class URL(models.Model):
    original = models.TextField(verbose_name='original link', blank=False, unique=False)
    short = models.CharField(verbose_name='short link', max_length=8, blank=False, unique=True)
    created_at = models.DateTimeField(verbose_name='created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated', auto_now=True)
    last_used_at = models.DateTimeField(verbose_name='last used', blank=True, null=True)
    user = models.ForeignKey(verbose_name='user', to=BonzoUser, on_delete=models.CASCADE, related_name='urls',
                             null=True)

    def update_last_used_time(self):
        self.last_used_at = datetime.now()
