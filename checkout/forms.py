from django import forms
from .models import Order
from django.forms import Select
 
 
class MakePaymentForm(forms.Form):
    
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2036)]
   
    credit_card_number = forms.CharField(label ='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput, required=False)
 
class OrderCreateForm(forms.ModelForm):
    

    class Meta:
        # COUNTRY_CHOICES = [('Australia', 'Australia') 'Austria', 'Belgium', 'Canada', 'Denmark', 'Finland', 'France',
        # 'Germany', 'Hong Kong', 'Ireland', 'Japan', 'Luxembourg', 'Netherlands', 'New Zealand', 'Norway',
        # 'Singapore', 'Spain', 'Sweden', 'Switzerland', 'United Kingdom', 'United States', 'Italy','Portugal',
        # 'Poland'
        # ]
        
        model = Order
        fields = ('full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1',
        'street_address2', 'county')
        # widgets = {'country': Select( choices=COUNTRY_CHOICES) }