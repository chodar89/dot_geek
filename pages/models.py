from django.db import models

class IndexCarousel(models.Model):
    image = models.ImageField(upload_to='photos/carousel')
    heading = models.CharField(max_length=150, blank=True)
    paragraph = models.CharField(max_length=300, blank=True)
    first = models.BooleanField(default=False)
    def __str__(self):
        return self.heading
