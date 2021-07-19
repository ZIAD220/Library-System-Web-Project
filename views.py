from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .forms import CreateSignupForm, UserUpdateForm,BookForm
from .filters import BookFilter

def index(request):
    return render(request, 'pages/index.html')

def aboutus(request):
    return render(request, 'pages/aboutus.html')

def adminsignup(request):
    form=CreateSignupForm()
    if request.method == 'POST':
        form = CreateSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
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

def studentsignup(request):
    form=CreateSignupForm()
    if request.method == 'POST':
        form = CreateSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
            return redirect('studentlogin')
    context={'form2':form}
    return render(request, 'pages/studentsignup.html',context)

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

def logoutuser(request):
    logout(request)
    return redirect('index')

@login_required(login_url='adminlogin')
def adminupdate(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Account information updated successfully')
            return redirect('adminupdate')
    else:
        form = UserUpdateForm(instance=request.user)
    context = {'form3':form}
    return render(request, 'pages/adminupdate.html',context)

@login_required(login_url='studentlogin')
def studentupdate(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Account information updated successfully')
            return redirect('studentupdate')
    else:
        form = UserUpdateForm(instance=request.user)
    context = {'form3':form}
    return render(request, 'pages/studentupdate.html',context)

@login_required(login_url='adminlogin')
def adminpage(request):
    return render(request,'pages/adminpage.html')

@login_required(login_url='studentlogin')
def studentpage(request):
    return render(request,'pages/studentpage.html')


@login_required(login_url='adminlogin')
def issuebook(request):
    return render(request,'pages/issuebook.html')

@login_required(login_url='adminlogin')
def viewissuedbook(request):
    return render(request,'pages/viewissuedbook.html')

@login_required(login_url='adminlogin')
def adminbooks(request):
    books = Book.objects.all()
    count = Book.objects.all().count()
    myFilter = BookFilter(request.GET,queryset=books)
    books = myFilter.qs
    context={'books':books,'count':count,'myFilter':myFilter}
    return render(request, 'pages/adminbooks.html',context)

@login_required(login_url='studentlogin')
def studentbooks(request):
    books = Book.objects.all()
    count = Book.objects.all().count()
    myFilter = BookFilter(request.GET,queryset=books)
    books = myFilter.qs
    context={'books':books,'count':count,'myFilter':myFilter}
    return render(request, 'pages/studentbooks.html',context)

@login_required(login_url='adminlogin')
def addBook(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST)
        if add_book.is_valid():
            add_book.save()
            return redirect('adminbooks')
    context = {'form' : BookForm()}
    return render(request, 'pages/addbook.html', context)

@login_required(login_url='adminlogin')
def updatebook(request,id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('adminbooks')
    else:
        book_save = BookForm(instance=book_id)
    context = {'form4' : book_save}
    return render(request, 'pages/updatebook.html', context)