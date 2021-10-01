from django.db import models
from django.utils import timezone

class Items(models.Model):
    item_id=models.AutoField(primary_key=True)
    item_name=models.CharField(max_length=100)
    price=models.IntegerField(null=True)
    def __str__(self):
        return self.item_name

class SupermarketModel(models.Model):
    id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=100)
    customer_mobile=models.CharField(max_length=10)
    customer_address=models.CharField(max_length=100)
    item=models.ForeignKey(Items,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.customer_name

class CustomerBill(models.Model):
    customer_name=models.CharField(max_length=100)
    customer_mobile=models.CharField(max_length=10)
    customer_address=models.CharField(max_length=100)
    item_name=models.CharField(max_length=100)
    unit_price=models.IntegerField(null=True)
    quantity=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    total_price=models.FloatField()
    def __str__(self):
        return self.customer_name







# Create your models here.


# Create your models here.
