from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Book
from .forms import CreateAdminForm

def index(request):
    return render(request, 'pages/index.html')

def aboutus(request):
    return render(request, 'pages/aboutus.html')

def adminsignup(request):
    form=CreateAdminForm()
    if request.method == 'POST':
        form = CreateAdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminlogin')
    context={'form1':form}
    return render(request, 'pages/adminsignup.html',context)

def adminlogin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('adminpage')
        else:
            messages.info(request,'Username or Password is incorrect')
    return render(request, 'pages/adminlogin.html')

def studentlogin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('studentpage')
        else:
            messages.info(request,'Username or Password is incorrect')
    return render(request, 'pages/studentlogin.html')

def studentsignup(request):
    form=CreateAdminForm()
    if request.method == 'POST':
        form = CreateAdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentlogin')
    context={'form2':form}
    return render(request, 'pages/studentsignup.html',context)

def logoutuser(request):
    logout(request)
    return redirect('index')

@login_required(login_url='adminlogin')
def adminpage(request):
    return render(request,'pages/adminpage.html')

@login_required(login_url='studentlogin')
def studentpage(request):
    return render(request,'pages/studentpage.html')

@login_required(login_url='adminlogin')
def bookadded(request):
    return render(request,'pages/bookadded.html')

@login_required(login_url='adminlogin')
def bookissued(request):
    return render(request,'pages/bookissued.html')

@login_required(login_url='adminlogin')
def issuebook(request):
    return render(request,'pages/issuebook.html')

@login_required(login_url='adminlogin')
def viewissuedbook(request):
    return render(request,'pages/viewissuedbook.html')

def viewbook(request):
    books=Book.objects.all()
    count=Book.objects.all().count()
    context={'books':books,'count':count}
    return render(request, 'pages/viewbook.html',context)