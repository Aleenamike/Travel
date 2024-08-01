from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('reg/',views.userregistration),
    path('log/',views.login), 
    path('cnt/',views.contact), 
    path('lcnt/',views.lcontact), 
    path('package/',views.packages),
    path('abt/',views.abouts),
    path('labt/',views.labouts),
    path('user/',views.user),
    path('adminpage/',views.adminpage),
    path('add_packages/',views.add_packages),
    path('pckdetails/<id>/',views.pckdetails),
    path('booking/<id>/',views.booking),
    path('profile/',views.profile),
    path('edtprof/',views.editprofile),
    path('bookings/',views.bookings),
    path('changepass/',views.changepass),
    path('vbook/',views.view_bookings),
    path('contacts/',views.contacts),
    path('mes/<id>/',views.messages),

]