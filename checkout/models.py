from django.db import models
from products.models import Product


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank='false')
    phone_number = models.CharField(max_length=20, blank='false')
    country = models.CharField(max_length=20, blank='false')
    postcode = models.CharField(max_length=10, blank='true')
    town_or_city = models.CharField(max_length=50, blank='false')
    street_address1 = models.CharField(max_length=50, blank='false')
    street_address2 = models.CharField(max_length=50, blank='false')
    county = models.CharField(max_length=50, blank='false')
    date = models.DateField()
   
    def __str__(self):
       return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)

       
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null="false")
    product = models.ForeignKey(Product, null="false")
    quantity = models.IntegerField(blank="false")
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)        
    
    
    
