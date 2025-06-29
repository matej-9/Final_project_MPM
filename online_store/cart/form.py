
from django import forms
from django.forms import CharField, TextInput


class ShippingAddressForm(forms.ModelForm):
    first_name = CharField(
        label='Meno',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Meno'
        })
    )

    last_name = CharField(
        label='Priezvisko',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Priezvisko'
        })
    )

    phone_number = CharField(
        label='Telefónne číslo',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Telefónne číslo'
        })
    )

    country = CharField(
        label='Krajina',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Krajina'
        })
    )

    city = CharField(
        label='Mesto',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mesto'
        })
    )

    street = CharField(
        label='Ulica a popisné číslo',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ulica a popisné číslo'
        })
    )

    zip_code = CharField(
        label='PSČ',
        required=True,
        max_length=5,
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'PSČ',
            'maxlength': '5'
        })
    )
