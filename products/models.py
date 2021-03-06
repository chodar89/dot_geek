from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from pages.models import IndexCarousel


class ProductType(models.Model):
    """ Product types model with option to show in the dropdown nav bar """
    types = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    is_in_navbar_menu = models.BooleanField(default=True)

    def __str__(self):
        return self.types


class ProductBrand(models.Model):
    """ Product brands model with option to show in the dropdown nav bar """
    brand_name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    is_in_navbar_menu = models.BooleanField(default=True)

    def __str__(self):
        return self.brand_name


class SizeChart(models.Model):
    """ Size chart for clothes """
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size


class Product(models.Model):
    """ Models for single prduct, with option to be in sale or no """
    product_type = models.ForeignKey(
        ProductType, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=70)
    brand = models.ForeignKey(ProductBrand, blank=True,
                              null=True, on_delete=models.SET_NULL)
    character = models.TextField(max_length=100, blank=True)
    series = models.TextField(max_length=100, blank=True)
    description = models.TextField(max_length=500, blank=True)
    short_description = models.TextField(max_length=180, blank=True)
    carousel = models.ForeignKey(IndexCarousel, blank=True, null=True, on_delete=models.CASCADE)
    buys = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    price = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name='GBP Price')
    stock = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(9999)])
    stock_xs = models.PositiveIntegerField(default=0, verbose_name='Stock Size XS', validators=[
                                           MinValueValidator(0), MaxValueValidator(9999)])
    stock_s = models.PositiveIntegerField(default=0, verbose_name='Stock Size S', validators=[
                                          MinValueValidator(0), MaxValueValidator(9999)])
    stock_m = models.PositiveIntegerField(default=0, verbose_name='Stock Size M', validators=[
                                          MinValueValidator(0), MaxValueValidator(9999)])
    stock_l = models.PositiveIntegerField(default=0, verbose_name='Stock Size L', validators=[
                                          MinValueValidator(0), MaxValueValidator(9999)])
    stock_xl = models.PositiveIntegerField(default=0, verbose_name='Stock Size XL', validators=[
                                           MinValueValidator(0), MaxValueValidator(9999)])
    stock_xxl = models.PositiveIntegerField(default=0, verbose_name='Stock Size XXL', validators=[
                                            MinValueValidator(0), MaxValueValidator(9999)])
    stock_xxxl = models.PositiveIntegerField(default=0, verbose_name='Stock Size XXXL', validators=[
                                             MinValueValidator(0), MaxValueValidator(9999)])
    # Add all sizes stock and pass it as property
    @property
    def total_stock(self):
        return self.stock + self.stock_xs + self.stock_s + self.stock_m + self.stock_l + self.stock_xl + self.stock_xxl + self.stock_xxxl
    photo_main = models.ImageField(upload_to='photos/products/%Y/%m/%d')
    photo_1 = models.ImageField(
        upload_to='photos/products/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(
        upload_to='photos/products/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(
        upload_to='photos/products/%Y/%m/%d', blank=True)
    is_for_sale = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
