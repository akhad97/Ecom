from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import *


PAYMENT_CHOICES = (
    ('C', 'Click'),
    ('P', 'Payme'),
)


class PaymentForm(forms.Form):
    class Meta:
        model = Payment
        fields = ('card_number', 'exp_data', 'security_number')

        card_number = forms.CharField( required=True, widget=forms.TextInput(attrs={
        'placeholder': '4646113212',
        'class': 'form-control'
    }))

class CheckoutForm(forms.Form):
    
    street_address = forms.CharField( required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Nukus st 102..',
        'class': 'form-control'
    }))
    apartment_address = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Apartment or suite',
        'class': 'form-control'
    }))
    region = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Tashkent...',
        'class': 'form-control'
    }))
    district = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Mirabad...',
        'class': 'form-control'
    }))
    zip = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES, required=True)

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
