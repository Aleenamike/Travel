from django.shortcuts import render,redirect
from myapp.models import *
import random,pyttsx3
from datetime import datetime
# Create your views here.
def index(request):
    pck=Packages.objects.all()
    return render(request,"index2.html",{'pck':pck})
def userregistration(request):
    if request.method=="POST":
        f=request.POST.get('fname')
        e=request.POST.get('email')
        a=request.POST.get('address')
        p=request.POST.get('phno')
        pc=request.POST.get('pin')
        pl=request.POST.get('place')
        un=request.POST.get('uname')
        pw=request.POST.get('password')
        da=travel(fname=f,email=e,address=a,phoneno=p,pincode=pc,place=pl,username=un,password=pw)
        da.save()
        return redirect('/log/')
    return render(request,"reg1.html")




def login(request):

    if request.method=="POST":
        u=request.POST.get('username')
        ps=request.POST.get('password')
        log = travel.objects.filter(username=u,password=ps)

        for i in log:
            ids=i.id
            email=i.email
            username=i.username
            password=i.password
            r=i.rights

            request.session['ids'] = ids
            request.session['email'] = email
            request.session['username'] = username
            request.session['password'] = password
            request.session['rights']=r
        if log.filter(username=u,password=ps).exists():
            for j in log:
                r=j.rights
            if r=='user':
                 return redirect('/user/')
            elif r=='admin':
                 return redirect('/adminpage/')
            else:
                print('invalid user')

    return render(request,"log.html")
def contact(request):
    username=request.session['username']
    msgs=''
    if request.method=="POST":
        name=request.POST.get('fname')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        msg=request.POST.get('msg')
        con=Contact(username=username,fullname=name,email=email,phno=phno,message=msg)
        con.save()
        msgs='success'
    return render(request,"cnt.html",{'msgs':msgs})

def lcontact(request):
    username=request.session['username']
    msgs=''
    if request.method=="POST":
        name=request.POST.get('fname')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        msg=request.POST.get('msg')
        con=Contact(username=username,fullname=name,email=email,phno=phno,message=msg)
        con.save()
        msgs='success'
    return render(request,"lcnt.html",{'msgs':msgs})

def packages(request):
    pck=Packages.objects.all()
    return render(request,"trpackage.html",{'pck':pck})
def abouts(request):
    return render(request,"about.html")

def labouts(request):
    return render(request,"labout.html")

def user(request):
    pck=Packages.objects.all()
    return render(request,'tdashboard.html',{'pck':pck})

def adminpage(request):
    pck=Packages.objects.all()
    return render(request,'adminpage.html',{'pck':pck})

def add_packages(request):
    if request.method=="POST":
        image=request.FILES['file']
        pname=request.POST.get('pname')
        days=request.POST.get('days')
        country=request.POST.get('country')
        place=request.POST.get('place')
        rate=request.POST.get('rate')
        desc=request.POST.get('description')
        pid=random.randint(000000,999999)
        pack=Packages(pid=pid,pimage=image,pckname=pname,pdays=days,pcountry=country,pplace=place,prate=rate,description=desc)
        pack.save()
    return render(request,'add_packages.html')

def pckdetails(request,id):
    pck=Packages.objects.filter(id=id)
    return render(request,'pckdetail.html',{'pck':pck})

def booking(request,id):
    username=request.session['username']
    pck=Packages.objects.filter(id=id)
    cdate=datetime.now().date()
    msg=''
    err=''
    for i in pck:
        pid=i.pid
    if request.method=="POST":
        fname=request.POST.get('fname')
        checkin=request.POST.get('check')
        cno=request.POST.get('cno')
        cvv=request.POST.get('cvv')
        exp=request.POST.get('exp')
        bid=random.randint(00000,99999)
        checkin=datetime.strptime(checkin,'%Y-%m-%d').date()
        if cdate<checkin:
            bk=Bookings(username=username,bid=bid,pid=pid,fullname=fname,checkin=checkin,cno=cno,cvv=cvv,exp=exp)
            bk.save()
            msg='success'
            # return redirect('/user/')
        else:
            err='Select a valid date!'
        
    return render(request,'booking.html',{'pck':pck,'msg':msg,'err':err})

def profile(request):
    username=request.session['username']
    tr=travel.objects.filter(username=username)
    return render(request,'profile.html',{'tr':tr})

def editprofile(request):
    username=request.session['username']
    tr=travel.objects.filter(username=username)
    if request.method=="POST":
        fname=request.POST.get('fname')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        travel.objects.filter(username=username).update(fname=fname,email=email,phoneno=phno)
    return render(request,'editprofile.html',{'tr':tr})

def bookings(request):
    username=request.session['username']
    details=[]
    bk=Bookings.objects.filter(username=username)
    for i in bk:
        pid=i.pid
        pck=Packages.objects.get(pid=pid)
        details.append({'pck':pck,'bk':i})
    return render(request,'bookings.html',{'details':details})

def changepass(request):
    password=request.session['password']
    username=request.session['username']
    if request.method=="POST":
        cpass=request.POST.get('cpass')
        npass=request.POST.get('npass')
        rpass=request.POST.get('rpass')
        if cpass!=password:
            engine=pyttsx3.init()
            msg='Wrong Password'
            engine.say(msg)
            engine.runAndWait()
        elif npass!=rpass:
            engine=pyttsx3.init()
            msg='Password Mismatch'
            engine.say(msg)
            engine.runAndWait()
        else:
            travel.objects.filter(username=username).update(password=rpass)
            return redirect('index')
    return render(request,'changepass.html') 

def view_bookings(request):
    details=[]
    bk=Bookings.objects.all()
    for i in bk:
        pid=i.pid
        pck=Packages.objects.get(pid=pid)
        details.append({'bk':i,'pck':pck})
    return render(request,'view_bookings.html',{'details':details})

def contacts(request):
    con=Contact.objects.all()
    return render(request,'contacts.html',{'con':con})

def messages(request,id):
    con=Contact.objects.filter(id=id)
    return render(request,'messages.html',{'con':con})