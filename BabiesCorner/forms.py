from django import forms
from .models import ShippingAddress


STATE_CHOICES = (
    ('Abia', 'Abia'), ('Adma', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia'), 
)

class ShippingAddressForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Firstname'}), label="")
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Lastname'}), label="")
    apartment = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Apartment, suite, etc'}), label="")
    street_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address'}), label="")
    state = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'placeholder': 'State'}), label="")
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Postal code'}), label="")
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}), label="")
    extra = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'Extra Information'}), label="")

    class Meta:
        model = ShippingAddress
        fields = ['firstname', 'lastname', 'apartment', 'street_address', 'state', 'postal_code', 'phone', 'extra']
