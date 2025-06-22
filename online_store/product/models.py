from django.db.models import Model, CharField, TextField, IntegerField, ImageField, ForeignKey, SET_NULL

class Category(Model):
    name = CharField(max_length=64, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"Category name: {self.name}"


class Product(Model):
    name = CharField(max_length=64, null=False, blank=False)
    desc = TextField(max_length=1024, null=True, blank=True)
    price = IntegerField(null=False, blank=False)
    quantity = IntegerField(null=True)
    image = ImageField(upload_to='images/', null=True, blank=True)
    category = ForeignKey(Category, on_delete=SET_NULL, related_name='products', null=True)


    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Products'

    def __repr__(self):
        return f"Product name: {self.name}, quantity: {self.quantity}, price: {self.price}"

    def __str__(self):
        return f"{self.name} {self.quantity} {self.price}"
    
