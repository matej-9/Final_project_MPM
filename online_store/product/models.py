from django.db.models import Model, CharField, TextField, IntegerField, ImageField

class Product(Model):
    name = CharField(max_length=64, null=False, blank=False)
    desc = TextField(max_length=256, null=True, blank=True)
    price = IntegerField(null=False, blank=False)
    quantity = IntegerField(null=True)
    image = ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Products'

    def __repr__(self):
        return f"Product name: {self.name}, quantity: {self.quantity}, price: {self.price}"

    def __str__(self):
        return f"{self.name} {self.quantity} {self.price}"