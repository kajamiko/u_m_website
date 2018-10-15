from django import forms
from material import *

DONATION_VALUE_CHOICES = [(i, str(i)) for i in range(5, 100, 5)]

class CartAddTicketForm(forms.Form):
     
     donation = forms.ChoiceField(choices=DONATION_VALUE_CHOICES, label='£', initial=0, required=True)
          
     update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
     
     