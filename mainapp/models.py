from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='name', max_length=64, unique=True)
    description = models.TextField(verbose_name='description', blank=True)
    is_active = models.BooleanField(verbose_name='active', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Product name', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='min info', max_length=60, blank=True)
    description = models.TextField(verbose_name='max info', blank=True)
    price = models.DecimalField(verbose_name='price', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='warehouse', default=0)
    is_active = models.BooleanField(verbose_name='active', default=True)

    def __str__(self):
        return f"{self.name}({self.category.name})"
