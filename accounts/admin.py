from django.contrib import admin
from .models import Profile


 
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1',
                    'street_address2', 'county']
    list_filter = ['user', 'full_name', 'country']
 
 
admin.site.register(Profile, ProfileAdmin)