from django import forms
from .models import Order
from django.forms import Select
 

 
class OrderCreateForm(forms.ModelForm):
    

    class Meta:
        COUNTRY_CHOICES = (('Australia', 'Australia'), ('Austria', 'Austria'), ('Belgium', 'Belgium'), ('Canada', 'Canada'), 
        ('Denmark', 'Denmark'), ('Finland', 'Finland'), ('France', 'France'),
        ('Germany', 'Germany'), ('Hong Kong', 'Hong Kong'), ('Ireland', 'Ireland'), ('Japan', 'Japan'), 
        ('Luxembourg', 'Luxembourg'), ('Netherlands', 'Netherlands'), ('New Zealand', 'New Zealand'), ('Norway', 'Norway'),
        ('Singapore', 'Singapore'), ('Spain', 'Spain'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), 
        ('United Kingdom', 'United Kingdom'), ('United States', 'United States'),('Italy', 'Italy'),('Portugal', 'Portugal'),
        ('Poland', 'Poland')
        )
        
        model = Order
        

        widgets = {'country': Select( choices=COUNTRY_CHOICES), 'user': forms.HiddenInput() }
        fields = ('user', 'full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1',
        'street_address2', 'county')
