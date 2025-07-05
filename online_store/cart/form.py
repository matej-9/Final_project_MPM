
from django import forms
from django.forms import CharField, TextInput


class ShippingAddressForm(forms.Form):
    first_name = CharField(
        label='Meno',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Meno'
        })
    )

    last_name = CharField(
        label='Priezvisko',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Priezvisko'
        })
    )

    phone_number = CharField(
        label='Telefónne číslo',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Telefónne číslo'
        })
    )

    country = CharField(
        label='Krajina',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Krajina'
        })
    )

    city = CharField(
        label='Mesto',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Mesto'
        })
    )

    street = CharField(
        label='Ulica a popisné číslo',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ulica a popisné číslo'
        })
    )

    zip_code = CharField(
        label='PSČ',
        required=True,
        max_length=5,
        widget=TextInput(attrs={
            'placeholder': 'PSČ',
            'maxlength': '5'
        })
    )
