from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

class ProductType(models.Model):
    product_type = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.product_type

class SizeChart(models.Model):
    size = models.CharField(max_length=10)
    def __str__(self):
        return self.size

class Product(models.Model):
    type_code = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    description = models.TextField()
    buys = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=4, decimal_places=2)
    size = models.ForeignKey(SizeChart, on_delete=models.DO_NOTHING, default=11)
    stock = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9999)])
    photo_main = models.ImageField(upload_to='photos')
    photo_1 = models.ImageField(upload_to='photos', blank=True)
    photo_2 = models.ImageField(upload_to='photos', blank=True)
    photo_3 = models.ImageField(upload_to='photos', blank=True)
    photo_4 = models.ImageField(upload_to='photos', blank=True)
    photo_5 = models.ImageField(upload_to='photos', blank=True)
    is_for_sale = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name
