from django.contrib.auth import logout
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('adminsignup', views.adminsignup, name='adminsignup'),
    path('studentlogin', views.studentlogin, name='studentlogin'),
    path('studentsignup', views.studentsignup, name='studentsignup'),
    path('logout',views.logoutuser, name='logout'),
    path('adminpage', views.adminpage, name='adminpage'),
    path('studentpage', views.studentpage, name='studentpage'),
    path('bookadded', views.bookadded, name='bookadded'),
    path('bookissued', views.bookissued, name='bookissued'),
    path('issuebook', views.issuebook, name='issuebook'),
    path('issuedbooks', views.viewissuedbook, name='viewissuedbook'),
    path('books', views.viewbook, name='viewbook'),
]