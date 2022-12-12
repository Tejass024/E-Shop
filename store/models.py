from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default="", null=True, blank=True)
    image = models.ImageField(upload_to='products/', height_field=None, width_field=None, max_length=None)
    
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    

    
    