from django.db import models
from datetime import datetime,timedelta

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.PositiveIntegerField()
    publicationYear=models.PositiveIntegerField()
    categories= [
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Comics', 'Comics'),
        ('Biography', 'Biographie'),
        ('History', 'History'),
    ]
    category = models.CharField(max_length=50, choices = categories)
    def __str__(self):
        return str(self.name)+" ["+str(self.isbn)+']'
    class Meta:
        ordering=['isbn']

def get_expiry():
    return datetime.today() + timedelta(days=15)
class BorrowedBook(models.Model):
    books = models.OneToOneField(Book, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    isbn = models.PositiveIntegerField()
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=get_expiry)
    def __str__(self):
        return self.books.name