from __future__ import unicode_literals

from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=False)
    store_name = models.CharField(max_length=250, blank=False, unique=True)
    price = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)
