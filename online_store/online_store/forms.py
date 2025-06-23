from django import forms

class ContactForm(forms.Form):
    firstname = forms.CharField(max_length=200)
    lastname = forms.CharField(max_length=200)
    email = forms.EmailField()