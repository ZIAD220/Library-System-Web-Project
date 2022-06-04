from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Book, BorrowedBook

class CreateSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name','isbn','publicationYear','author','category']
        widgets = {
            'category':forms.Select(attrs={'class':'form-control'})
        }

class BorrowForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = ['books','name','isbn','expirydate']
        widgets = {
            'books':forms.Select(attrs={'class':'form-control'})
        }