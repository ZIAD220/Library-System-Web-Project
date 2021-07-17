from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .models import *
from .forms import CreateAdminForm

def index(request):
    return render(request, 'pages/index.html')

def aboutus(request):
    return render(request, 'pages/aboutus.html')

def adminlogin(request):
    return render(request, 'pages/adminlogin.html')

def adminsignup(request):
    form = CreateAdminForm()
    if request.method=='post':
        form=CreateAdminForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'pages/adminsignup.html',context)

def studentlogin(request):
    return render(request, 'pages/studentlogin.html')

def studentsignup(request):
    context = {}
    return render(request, 'pages/studentsignup.html',context)

def adminafterlogin(request):
    return render(request, 'pages/adminafterlogin.html')

def studentafterlogin(request):
    return render(request, 'pages/studentafterlogin.html')

def bookadded(request):
    return render(request, 'pages/bookadded.html')

def bookissued(request):
    return render(request, 'pages/bookissued.html')

def issuebook(request):
    return render(request, 'pages/issuebook.html')

def viewissuedbook(request):
    return render(request, 'pages/viewissuedbook.html')

def viewbook(request):
    return render(request, 'pages/viewbook.html',{'books':Book.objects.all()})