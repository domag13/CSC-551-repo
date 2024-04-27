from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated', 'customer_id']
    inlines = [OrderItemInline]

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
    'address', 'address_2', 'postal_code', 'city', 'state', 'phone']
    list_filter = ['id', 'first_name', 'last_name']

    