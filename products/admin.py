from django.contrib import admin

from .models import Product, ProductType, SizeChart, ProductBrand

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_type', 'brand', 'stock', 'buys', 'is_for_sale')
    list_display_links = ('id', 'name')
    list_filter = ('product_type', 'brand')
    list_editable = ('is_for_sale', 'stock')
    search_fields = ('name', 'description', 'series', 'character', 'short_description')
    list_per_page = 50

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brands', 'description')
    list_display_links = ('id', 'brands')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'types', 'description')
    list_display_links = ('id', 'types')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, TypeAdmin)
admin.site.register(SizeChart)
admin.site.register(ProductBrand, BrandAdmin)
