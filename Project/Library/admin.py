from django.contrib import admin
from .models import Book,BorrowedBook

admin.site.register(Book)
admin.site.register(BorrowedBook)