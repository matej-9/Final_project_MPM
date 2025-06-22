from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, ImageField, \
    TextField, CharField


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE, unique=True)
    phone_number = CharField(max_length=20, blank=True)
    country = TextField(null=True, blank=True)
    city = TextField(null=True, blank=True)
    street = TextField(null=True, blank=True)
    zip_code = CharField(max_length=5, null=True, blank=True)

    class Meta:
        ordering = ['user__username']

    def __repr__(self):
        return f"Profile(user={self.user})"

    def __str__(self):
        return self.user.username

