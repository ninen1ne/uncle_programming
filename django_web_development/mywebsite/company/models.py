from django.db import models

# Create your models here.(database)

"""
Product(name of table)
    - title (Char)
    - description (Text)
    - price (Decimal)
    - quantity (Int)
"""

"""
After create or change models run 2 commands from terminal:
1) python manage.py makemigrations
2) python manage.py migrate
"""

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title