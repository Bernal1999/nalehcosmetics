from django.db import models

# Create your models here.

class Product (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='products/',blank=True,null=True)

    def __str__(self):
        return self.title

class NewProducts(models.Model):
    image = models.ImageField(upload_to='producs/',blank=True,null=True)
    title = models.CharField(max_length=200,blank=True,null=True)
    description = models.CharField(max_length=300,blank=True,null=True)