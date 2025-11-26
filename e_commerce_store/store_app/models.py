from django.db import models

# Create your models here.
# product model
class Product(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits = 8, decimal_places= 2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
# cart item model
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def  total_price(self):
        return self.quantity * self.product.price
    