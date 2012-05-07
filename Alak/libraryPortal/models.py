from django.db import models
from Alak.home.models import UserProfile

class Book(models.model):
    name = models.CharField(max_length=400, required=True)
    author = models.CharField(max_length=400, required=False)
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


