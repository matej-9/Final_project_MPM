from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    firstname = forms.CharField(max_length=200)
    lastname = forms.CharField(max_length=200)
    email = forms.EmailField(validators=[EmailValidator(message="Enter a valid email address.")])
    content = forms.CharField(widget=forms.Textarea)