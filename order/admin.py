from django.contrib import admin
from .models import OrderItem, Order

# Register your models here.


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
        ('Product', {'fields': ['product'], }),
        ('Qynatity', {'fields': ['quantity'], }),
        ('Size', {'fields': ['item_size'], }),
        ('Price', {'fields': ['price'], }),
    ]
    readonly_fields = ('product', 'quantity', 'price', 'item_size')
    can_delete = False
    max_num = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'billing_name', 'email_address', 'user', 'created_at')
    list_display_links = ('id', 'billing_name', 'email_address')
    search_fields = ('id', 'billing_name', 'email_address', 'user__username')
    readonly_fields = ('id', 'token', 'total', 'email_address', 'created_at', 'billing_name', 'billing_address1', 'billing_city',
                       'billing_postcode', 'billing_country', 'shipping_name', 'shipping_address1', 'shipping_city', 'shipping_postcode', 'shipping_country')
    fieldsets = [
        ('ORDER INFORMATION', {'fields': [
         'id', 'token', 'total', 'created_at', 'email_address']}),
        ('BILLING INFORMATION', {'fields': [
         'billing_name', 'billing_address1', 'billing_city', 'billing_postcode', 'billing_country']}),
        ('SHIPPING INFORMATION', {'fields': [
         'shipping_name', 'shipping_address1', 'shipping_city', 'shipping_postcode', 'shipping_country']}),
    ]

    inlines = [
        OrderItemAdmin,
    ]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
