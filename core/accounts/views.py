from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm
from . models import User



def index(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form =UserRegistrationForm(request.POST)        
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username,email=email,phone=phone,password=password)
            user.save()
            messages.success(request, 'You have been successfully registered')
            return redirect('login')        
    
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/registration.html',{'form':form})



def login_user(request):
    if request.method=='POST':        
        email=request.POST['email']        
        password=request.POST['password']
        user= authenticate(request, email=email,password=password)
        if user is not None:
            print(user)
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Inavlid login credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect('login')

