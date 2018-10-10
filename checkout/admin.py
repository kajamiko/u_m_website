from django.contrib import admin
from .models import Order, OrderItem
 
 
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['ticket']
 
 
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1',
                    'street_address2', 'county']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
 
 
admin.site.register(Order, OrderAdmin)