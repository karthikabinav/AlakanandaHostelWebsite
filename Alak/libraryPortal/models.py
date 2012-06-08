from django.db import models
from Alak.home.models import UserProfile

class Book(models.Model):
    name = models.CharField(max_length=400)
    author = models.CharField(max_length=400)
    isVisible = models.BooleanField()
    
    def __unicode__(self):
        return self.name
    
    class Admin:
        pass
    
class BookOrder(models.Model):
    user = models.ForeignKey(UserProfile)
    book = models.ForeignKey(Book)
    dateBorrowed = models.DateTimeField()
    dateReturned = models.DateTimeField(null=True)
    dueDate = models.DateTimeField()
        
    class Admin:
        pass

class ShippingKey(models.Model):
    key = models.CharField(max_length=100)
    
    class Admin:
        pass
    
class ShippingLogin(models.Model):
    user = models.ForeignKey(UserProfile)
    lastLogin = models.DateTimeField()
    
    class Admin:
        pass

class Shipping(models.Model):
    order = models.ForeignKey(BookOrder)
    type = models.CharField(max_length=10)
    shippedOn = models.DateTimeField()
    shippedBy = models.ForeignKey(ShippingLogin)
