from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10 ,decimal_places=2)
    product_details = models.TextField(max_length=500)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    stock = models.CharField(max_length=100)
    discount = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.product_name