from django.contrib import admin

from .models import Product, ProductType, SizeChart

admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(SizeChart)
