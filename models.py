from django.db import models
from datetime import datetime,timedelta

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    status_book = [
        ('available', 'available'),
        ('rental', 'rental'),
        ('sold', 'sold'),
    ]
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, null = True, blank = True)
    isbn=models.PositiveIntegerField()
    publicationYear=models.PositiveIntegerField()
    categories= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biographie'),
        ('history', 'History'),
    ]
    category = models.CharField(max_length=50, choices = categories, null = True, blank = True)
    active = models.BooleanField(default = True)
    def get_expiry():
        return datetime.today() + timedelta(days=15)
    #cover = models.ImageField(upload_to='photos', null = True, blank = True)
    #photo_author = models.ImageField(upload_to='photos', null = True, blank = True)
    #pages = models.IntegerField(null = True, blank = True)
    #price = models.DecimalField(max_digits = 5, decimal_places = 2, null = True, blank = True)
    #retal_price_day = models.DecimalField(max_digits = 5, decimal_places = 2, null = True, blank = True)
    #models.IntegerField(null = True, blank = True)
    #status = models.CharField(max_length = 50, choices = status_book, null = True, blank = True)
'''from django.db import models

class Book(models.Model):
    name=models.CharField(max_length=30)
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=category,default='education')
    active=models.BooleanField(default=True)
    def __str__(self):
        return str(self.name)
    class Meta:
        ordering=['isbn']
'''