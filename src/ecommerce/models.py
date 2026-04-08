from django.db import models

# Create your models here.
class ProductModel(models.Model):
    tittle = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10 , decimal_places=2)

    description = models.TextField(blank=True, null=True)
    seller = models.CharField(max_length=100, default="Vendedor Genérico")
    color = models.CharField(max_length=30, blank=True)
    product_dimensions = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.tittle
