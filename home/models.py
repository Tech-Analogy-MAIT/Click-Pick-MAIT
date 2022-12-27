from django.db import models

# Create your models here.
class Order(models.Model):
    order_id=models.CharField(max_length=100,default='1')
    order_name=models.CharField(max_length=1000)
    order_price=models.CharField(max_length=1000)

    def __str__(self):
        return self.order_name
