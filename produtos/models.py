from django.db import models


# Create your models here.
class Product(models.Model):
    name_product = models.CharField(max_length=255)
    cod_product = models.IntegerField()
    amount_product = models.IntegerField()
    prince_product = models.DecimalField(max_digits=7, decimal_places=2)
    img_product = models.ImageField(upload_to='produtos_photos', null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Produtos'
        verbose_name = 'Produtos'

    def __str__(self):
        return self.name_product
