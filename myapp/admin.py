from django.contrib import admin
from myapp.models import *

class traveladm(admin.ModelAdmin):
    List_display=('fname','email','phone no','address','pincode','place','code','username','password','rights')
admin.site.register(travel,traveladm)
admin.site.register(Packages)
admin.site.register(Bookings)
admin.site.register(Contact)
