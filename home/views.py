from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def index(request):  
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')
    # return HttpResponse('this is homepage')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('this is aboutpage')

def services(request):
    return render(request, 'services.html')
    # return HttpResponse('this is servicespage')
    
def Softy(request):
    return render(request, 'Softy.html')

def FamilyPack(request):
    return render(request, 'FamilyPack.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone= request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,desc=desc,date= datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
    # return HttpResponse('this is contactpage')
    
def loginUser(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        
        # check if user has enterd correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/')
        else:
        # No backend authenticated the credentials
            return render(request,'login.html')
        
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')