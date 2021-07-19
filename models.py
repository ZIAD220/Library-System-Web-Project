from django.db import models

from django.db import models
from datetime import datetime,timedelta

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn=models.PositiveIntegerField()
    publicationYear=models.PositiveIntegerField()
    categories= [
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Comics', 'Comics'),
        ('Biography', 'Biographie'),
        ('History', 'History'),
    ]
    category = models.CharField(max_length=50, choices = categories)
    active = models.BooleanField(default = True)
    def __str__(self):
        return str(self.name)
    class Meta:
        ordering=['isbn']