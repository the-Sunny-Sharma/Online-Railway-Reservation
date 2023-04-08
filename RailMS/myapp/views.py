from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from django.contrib import messages
from myapp.models import BookTicket,Chart,Register,Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.template import Template, Context
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')


def view_schedule(request):
    schedule=Chart.objects.all()
    return render(request, 'view_schedule.html', {'key1':schedule})


@login_required(login_url="login_user")
def pnr_status(request):
    if request.method == "POST":
        pnrNumber=request.POST['pnrNumber']
        mydata = BookTicket.objects.filter(pnr_number=pnrNumber).values()
        template = loader.get_template('view_pnr.html')
        context = {
            'pnrStatus': mydata,
        }
        return HttpResponse(template.render(context, request))
        # data=BookTicket.objects.all()
        # return render(request,'view_pnr.html',{'pnrStatus':data})
    return render(request, 'pnr_status.html')


def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        comment=request.POST.get('comment')
        contact=Contact(name=name,email=email,comment=comment,date=datetime.today())
        contact.save()
        messages.success(request, 'Thank you your response is been sent. We\'ll get in touch soon.')
    return render(request, 'contact.html')


@login_required(login_url="login_user")
def bookTicket(request):
    if request.method == "POST":
        pnr_number=random.randint(1000000000,9999999999)
        pass1name=request.POST.get('pass1name')
        pass1age=request.POST.get('pass1age')
        pass1berth_opt=request.POST.get('pass1berth_opt')
        pass2name=request.POST.get('pass2name')
        pass2age=request.POST.get('pass2gage')
        pass2berth_opt=request.POST.get('pass2berth_opt')
        pass3name=request.POST.get('pass3name')
        pass3age=request.POST.get('pass3age')
        pass3berth_opt=request.POST.get('pass3berth_opt')
        source=request.POST.get('source')
        destination=request.POST.get('destination')
        dateJourney=request.POST.get('dateJourney')
        trainNumber=request.POST.get('trainNumber')
        bookTicket = BookTicket(trainNumber=trainNumber,dateJourney=dateJourney,destination=destination,source=source,pnr_number=pnr_number,pass1name=pass1name,pass1age=pass1age,pass1berth_opt=pass1berth_opt,pass2name=pass2name,pass2age=pass2age,pass2berth_opt=pass2berth_opt,pass3name=pass3name,pass3age=pass3age,pass3berth_opt=pass3berth_opt)
        bookTicket.save()
        Context={'pnr_number':pnr_number}
        messages.success(request, 'Thank you your response is been sent.')
        return render(request,'confirmBooking.html',Context)
    return render(request,'bookTicket.html')

    
@login_required(login_url="login_user")
def view_ticket(request):
  mydata = BookTicket.objects.filter(User).values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))


def register(request):
    if request.method == "POST":
        fname=request.POST.get('fname')
        mname =request.POST.get('mname')
        lname=request.POST.get('lname')
        mail=request.POST.get('mail')
        dob=request.POST.get('dob')
        phone=request.POST.get('phone')
        username=request.POST.get('username')
        password=request.POST.get('password')
        myuser = User.objects.create_user(username,mail,password)
        myuser.first_name = fname
        myuser.last_name=lname
        register=Register(fname=fname,mname=mname,lname=lname,mail=mail,dob=dob,phone=phone,username=username,password=password)
        register.save()
        myuser.save()
        messages.success(request, 'Your aaccount has been successfully created.')
        return redirect('login_user')
    return render(request, 'register.html')


def login_user(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request, "bookTicket.html",{'fname':fname})
        else:
            messages.error(request,"Bad Credential!")
            return redirect('login_user')
    return render(request,"login_user.html")


def logout_user(request):
    logout(request)
    return redirect('home')


def view_train(request):
    return render(request,"view_train.html")


def view_schedule(request):
    schedule=Chart.objects.all()
    return render(request, 'view_schedule.html', {'key1':schedule})


def admin(request):
    return render(request,"http://127.0.0.1:8000/admin")


def view_ticket(request):
    istekler = Contact.objects.all()
    return render(request, 'view_ticket.html', locals())


def confirmBooking(request):
    return redirect('home')


def view_pnr(request):
    return render("view_pnr.html")


# https://www.railmitra.com/trains