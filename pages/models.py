from django.db import models

# Create your models here.


class Product(models.Model):

    CATEGORY_CHOICES = [
        ('Men','Men'),
        ('Women','Women'),
        ('Kids','Kids'),
        ('Accesories','Accesories'),
        ('Cosmetic','Cosmetic')
    ]

    product_name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Accesories')
    product_details = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10 ,decimal_places=2)
    discount = models.DecimalField(max_digits=2, decimal_places=1)
    rating = models.IntegerField()
    


    def __str__(self):
        return self.product_name