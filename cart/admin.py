from django.contrib import admin

from .models import Cart, CartItem

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'cart_id', 'created_at')
    list_display_links = ('id', 'user', 'cart_id')
    search_fields = ('cart_id',)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product')
    list_display_links = ('id', 'cart')
    search_fields = ('cart', 'product')

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)