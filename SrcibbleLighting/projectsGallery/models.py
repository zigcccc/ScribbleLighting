from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Image(models.Model):
    image_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = '/uploads')

    def __str__(self):
        return self.image_title
