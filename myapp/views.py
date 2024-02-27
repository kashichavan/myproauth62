from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from .forms import *

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout
# Create your views here.


def register(request):
    if request.method=="POST":
            user=User.objects.filter(username=request.POST['username'])
            if user.exists():
                  messages.info(request,'User Laready exist')
                  return redirect(reverse('myapp:register'))

            form=RegistrationForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect(reverse('myapp:login'))
    f=RegistrationForm()
    return render(request,'register.html',context={'form':f})

def login_view(request):
    if request.method=='POST':
            form=LoginForm(request.POST)
            if form.is_valid():
                user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
                if user:
                      login(request,user)
                      return redirect(reverse('myapp:home'))
                else:
                      messages.error(request,'Invalid username or password')
                      return redirect(reverse('myapp:login'))
    f=LoginForm()
    return render(request,'login.html',context={'form':f})


login_required(login_url='myapp:login')
def home(request):
      return render(request,'home.html')

def logout_view(request):
      logout(request)
      return redirect(reverse('myapp:login'))



                  
            