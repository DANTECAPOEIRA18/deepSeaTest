from django.db import models
from django.utils.html import mark_safe
import base64
from rest_framework import serializers


# Create your models here.

class teams(models.Model):
    id = models.AutoField(primary_key=True)
    name_team = models.CharField(max_length=250, blank=False, null=False)
    date_create = models.DateField('Date Create', auto_now=True, auto_now_add=False)
    image_team = models.ImageField(upload_to='images/', null=True, blank=True)
    image_b64 = models.BinaryField(blank=True, null=True)

    @property
    def thumbnail_preview(self, *args, **kwargs):
        if self.image_team:
            # print(self.image_team.url)
            img_file = open(self.image_team.path, 'rb')
            self.image_b64 = base64.b64encode(img_file.read())
            super(teams, self).save(*args, **kwargs)
            return mark_safe(
                '<img src="data:;base64,{}" width="200" height="200" />'.format(self.image_b64.decode('utf-8')))
        return ""

    class Meta:
        verbose_name = 'Teams'
        verbose_name_plural = 'Team'
        ordering = ['name_team']

    def __str__(self):
        return self.name_team
