from django.db import models

# Create your models here.

class Customer(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  email = models.EmailField()

class Order(models.Model):
  product_name = models.CharField(max_length=200)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

  def __str__(self):
    return f'Order of {self.product_name} by {self.customer}'
  
  