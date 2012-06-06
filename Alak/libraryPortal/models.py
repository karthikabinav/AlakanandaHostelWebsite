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
    dueDate = models.DateTimeField()
    
    class Admin:
        pass


