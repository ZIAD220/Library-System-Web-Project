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
    path('adminupdate',views.adminupdate, name='adminupdate'),
    path('studentupdate',views.studentupdate, name='studentupdate'),
    path('<int:id>',views.updatebook, name='updatebook'),
    path('adminpage', views.adminpage, name='adminpage'),
    path('studentpage', views.studentpage, name='studentpage'),
    path('issuebook', views.issuebook, name='issuebook'),
    path('issuedbooks', views.viewissuedbook, name='viewissuedbook'),
    path('adminbooks', views.adminbooks, name='adminbooks'),
    path('studentbooks', views.studentbooks, name='studentbooks'),
    path('addbook', views.addbook, name='addbook'),
    path('borrowedbook', views.borrowedbook, name='borrowedbook'),
    path('borrow', views.borrowbook, name='borrowbook'),
    path('extendborrow/<int:id>', views.extendborrow, name='extendborrow'),
    path('returnborrow/<int:id>', views.returnborrow, name='returnborrow'),
]