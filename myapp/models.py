from django.db import models

class travel(models.Model):
    fname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=50,null=True)
    pincode=models.CharField(max_length=50,null=True)
    place=models.CharField(max_length=50,null=True)
    username=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
    rights=models.CharField(max_length=20,default='user')
    def __str__(self):
        return self.fname

class Packages(models.Model):
    pid=models.IntegerField()
    pimage=models.ImageField(upload_to='images/')
    pckname=models.CharField(max_length=50)
    pdays=models.IntegerField()
    pcountry=models .CharField(max_length=50)
    pplace=models .CharField(max_length=50)
    prate=models.IntegerField()
    description=models.TextField(max_length=100,null=True)

    def __str__(self):
        return self.pckname

class Bookings(models.Model):
    bid=models.IntegerField()
    bdate=models.DateField(auto_now_add=True,null=True)
    pid=models.IntegerField()
    username=models.CharField(max_length=50,null=True)
    fullname=models.CharField(max_length=50)
    checkin=models.DateField()
    cno=models.IntegerField()
    cvv=models.IntegerField()
    exp=models.DateField()

    def __str__(self):
        return self.fullname

class Contact(models.Model):
    username=models.CharField(max_length=50,default='')
    fullname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phno=models.CharField(max_length=50)
    message=models.TextField(max_length=200)

    def __str__(self):
        return self.fullname