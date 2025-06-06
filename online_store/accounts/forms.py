from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import CharField, PasswordInput, NumberInput, \
    Textarea

from accounts.models import Profile


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email',
                  'password1', 'password2']

        labels = {
            'username': 'Uživatelské jméno',
            'first_name': 'Jméno',
            'last_name': 'Příjmení',
            'email': 'E-mail'
        }

    password1 = CharField(
        widget=PasswordInput(attrs={'placeholder': 'Heslo'}),
        label='Heslo'
    )

    password2 = CharField(
        widget=PasswordInput(attrs={'placeholder': 'Heslo znovu'}),
        label='Heslo znovu'
    )

    country = CharField(
        widget=Textarea(attrs={
            'placeholder': 'Krajina',
            'class': 'form-control'}),
        label='Krajina',
        required=False
    )

    city = CharField(
        widget=Textarea(attrs={
            'placeholder': 'Mesto',
            'class': 'form-control'}),
        label='Mesto',
        required=False
    )

    street = CharField(
        widget=Textarea(attrs={
            'placeholder': 'Ulica a popisné číslo',
            'class': 'form-control'}),
        label='Ulica a popisné číslo',
        required=False
    )

    postal_code = CharField(
        widget=Textarea(attrs={'placeholder': 'PSČ','maxlength': '5'}),
        label='PSČ',
        required=False
    )

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        user = super().save(commit)  # vytvoríme uživatela

        # ešte potrebujeme vytvoriť Profile
        country = self.cleaned_data.get('country')
        city = self.cleaned_data.get('city')
        street = self.cleaned_data.get('street')
        postal_code = self.cleaned_data.get('postal_code')
        avatar = self.cleaned_data.get('avatar')
        user_profile = Profile(
            user=user,
            country=country,
            city=city,
            street=street,
            postal_code=postal_code,
            avatar=avatar
        )
        if commit:
            user_profile.save()
        return user