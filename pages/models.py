from django.db import models

from exclusivebooleanfield import ExclusiveBooleanField

class IndexCarousel(models.Model):
    image = models.ImageField(upload_to='photos/carousel')
    heading = models.CharField(max_length=150, blank=True)
    paragraph = models.CharField(max_length=300, blank=True)
    first = ExclusiveBooleanField()
