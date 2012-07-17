import os
from django.db import models
from django.conf import settings

class Slider(models.Model):
    images = models.ImageField(upload_to='slider')
    title = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.title
