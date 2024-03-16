from django.db import models


class Product(models.Model):

    product_title = models.CharField(max_length=100)
    product_desc = models.TextField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_category = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_title
