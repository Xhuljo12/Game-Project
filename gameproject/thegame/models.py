from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    product_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    product_image = models.ImageField(upload_to="media/")
    product_description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.product_name}'

class ProductBase(models.Model):
    productBase_id = models.AutoField(primary_key=True)
    productBase_name = models.CharField(max_length=100, null=True, blank=True)
    productBase_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    productBase_image = models.ImageField(upload_to="media/")
    productBase_description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.productBase_name}'

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=100, null=True, blank=True)
    contact_surname = models.CharField(max_length=100, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_message = models.TextField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return f'{self.contact_name} {self.contact_surname}'

class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    news_name = models.CharField(max_length=100, null=True, blank=True)
    news_image = models.FileField(upload_to="media/")
    news_description = models.TextField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return f'{self.news_name}'

class NewsBase(models.Model):
    newsBase_id = models.AutoField(primary_key=True)
    newsBase_name = models.CharField(max_length=100, null=True, blank=True)
    newsBase_image = models.ImageField(upload_to="media/")
    newsBase_description = models.TextField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return f'{self.newsBase_name}'