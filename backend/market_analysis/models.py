from django.db import models

class ProductPriceReference(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True)
    supplier = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    source = models.CharField(max_length=200, blank=True)
    observed_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product_name
