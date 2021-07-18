from django.db import models

class Book(models.Model):
    category= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biographie'),
        ('history', 'History'),
        ]
    name=models.CharField(max_length=30)
    isbn=models.PositiveIntegerField()
    publicationYear=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=category,default='education')
    active=models.BooleanField(default=True)
    def __str__(self):
        return str(self.name)
    class Meta:
        ordering=['isbn']