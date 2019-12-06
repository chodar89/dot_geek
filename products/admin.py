from django.contrib import admin

from .models import Product, ProductType, SizeChart, ProductBrand

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_type', 'brand', 'price', 'stock', 'buys', 'is_for_sale')
    list_display_links = ('id', 'name')
    list_filter = ('product_type', 'brand')
    list_editable = ('is_for_sale', 'stock', 'price')
    search_fields = ('name', 'description', 'series', 'character', 'short_description')
    readonly_fields = ('created_at',)
    list_per_page = 50


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_name', 'description', 'is_in_navbar_menu')
    list_editable = ('is_in_navbar_menu',)
    list_display_links = ('id', 'brand_name')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'types', 'description', 'is_in_navbar_menu')
    list_editable = ('is_in_navbar_menu',)
    list_display_links = ('id', 'types')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, TypeAdmin)
admin.site.register(SizeChart)
admin.site.register(ProductBrand, BrandAdmin)
