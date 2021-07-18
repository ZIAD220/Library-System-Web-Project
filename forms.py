from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import Book , Category
from django.contrib.auth.forms import UserCreationForm

class CreateSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
