# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ws_login_users(models.Model):
    created_at = models.IntegerField()
    use_at = models.IntegerField()
    deny_at = models.IntegerField()
    website_id = models.IntegerField()
    website_name = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)

    class Meta:
        db_table = 'ws_login_users'

