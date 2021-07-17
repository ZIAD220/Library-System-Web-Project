from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('adminsignup', views.adminsignup, name='adminsignup'),
    path('studentlogin', views.studentlogin, name='studentlogin'),
    path('studentsignup', views.studentsignup, name='studentsignup'),
    path('adminpage', views.adminafterlogin, name='adminafterlogin'),
    path('studentpage', views.studentafterlogin, name='studentafterlogin'),
    path('bookadded', views.bookadded, name='bookadded'),
    path('bookissued', views.bookissued, name='bookissued'),
    path('issuebook', views.issuebook, name='issuebook'),
    path('issuedbooks', views.viewissuedbook, name='viewissuedbook'),
    path('books', views.viewbook, name='viewbook'),
]