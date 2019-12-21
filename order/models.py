from django.db import models
from products.models import SizeChart
from django.contrib.auth.models import User

class Order(models.Model):
    token = models.CharField(max_length=250, blank=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='GBP Total Order')
    email_address = models.EmailField(max_length=250, blank=True, verbose_name='Email Address')
    created_at = models.DateField(auto_now_add=True)
    billing_name = models.CharField(max_length=250, blank=True)
    billing_address1 = models.CharField(max_length=250, blank=True)
    billing_city = models.CharField(max_length=250, blank=True)
    billing_postcode = models.CharField(max_length=10, blank=True)
    billing_country = models.CharField(max_length=200, blank=True)
    shipping_name = models.CharField(max_length=250, blank=True)
    shipping_address1 = models.CharField(max_length=250, blank=True)
    shipping_city = models.CharField(max_length=250, blank=True)
    shipping_postcode = models.CharField(max_length=10, blank=True)
    shipping_country = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='GBP Price')
    item_size = models.ForeignKey(SizeChart, blank=True, null=True, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def sub_total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.product
