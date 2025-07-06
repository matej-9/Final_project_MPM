# Create your tests here.

from django.test import TestCase
from django.contrib.auth.models import User
from accounts.forms import SignUpForm
from accounts.models import Profile


class SignUpFormTest(TestCase):
    def test_valid_signup_form_creates_user_and_profile(self):
        form_data = {
            'username': 'tester',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
            'phone_number': '+421944258222',
            'country': 'Slovensko',
            'city': 'Bratislava',
            'street': 'Hlavná 1',
            'zip_code': '81101',
        }

        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())

        user = form.save()

        # Otestuj vytvoreného užívateľa
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'tester')

        # Otestuj vytvorený profil
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.phone_number, '+421944258222')
        self.assertEqual(profile.country, 'Slovensko')
        self.assertEqual(profile.city, 'Bratislava')
        self.assertEqual(profile.street, 'Hlavná 1')
        self.assertEqual(profile.zip_code, '81101')

    def test_invalid_passwords(self):
        form_data = {
            'username': 'tester2',
            'password1': 'pass1',
            'password2': 'pass2',  # nezhodujú sa
        }
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_missing_required_fields(self):
        form = SignUpForm(data={})  # prázdny formulár
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password1', form.errors)

