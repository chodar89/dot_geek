from django.contrib import admin

from .models import Product, ProductType, SizeChart, ProductBrand

admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(SizeChart)
admin.site.register(ProductBrand)
