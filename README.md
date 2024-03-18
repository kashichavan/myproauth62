User Authentication and Authorization:
---------------------------------------------
Authentication: The process of validating user is called authentication.

Authorization: The process of validating access permissions of user is called authorization.


Generally our web pages can be accessed by any person without having any restrictions. 
But some times our business requirement is to access a web page compulsory we have to 
register and login.Then only end user can able to access our page. To fulfill such of 
requirements we should go for Django authentication and authorization module. 
(auth application).



User Registration:
----------------------

step 1) create a formclass in forms.py file
step 2) that class need to be modelform for the User[django.contrib.auth.models] class 
step 3) define the fields which are already predefined in User class


from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','password']

step 4) create a view in views.py file in app

step 5) first check request.method is post or not if it is post then create a object for 
	formclass by passing request.POST as arguement
step 6) then check form is valid or not.
	if it is valid then save() the form 
step 7) if we save passowrd will not be hashed to hash the password we need to override save() in form class.

	def save(self):
        s=super().save(commit=False)
        s.password=make_password(self.cleaned_data['password'])
        s.save()
        return s

forms.py
--------------


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','password']
    def save(self):
        s=super().save(commit=False)
        s.password=make_password(self.cleaned_data['password'])
        s.save()
        return s

views.py:
------------

from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from .forms import *

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
                  return redirect()
    f=RegistrationForm()
    return render(request,'register.html',context={'form':f})


User Login:
--------------

step 1) create a LoginForm class in forms.py

step 2) LoginForm class need to inherit from forms.Form class

step 3) go to views.py and create a view 

step 4)  first check request.method is post or not if it is post then create a object for Loginformclass by passing request.POST as arguement


step 5) check formclass is valid or not

step 6) if loginformclass is valid then we need to authenticate 


	user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])

step 7) check user is valid or notif it is valid the login(request,user)

	if user:
                login(request,user)
                return redirect(reverse('myapp:home'))
        else:
                messages.error(request,'Invalid username or password')
                return redirect(reverse('myapp:login'))


  Session Management:
---------------------
 Client and Server can communicate with some common language which is nothing but 
HTTP.

 The basic limitation of HTTP is, it is stateless protocol. i.e it is unable to remember 
client information for future purpose across multiple requests. Every request to the 
server is treated as new request.

Hence some mechanism must be required at server side to remember client 
information across multiple requests.This mechanism is nothing but session 
management mechanism.



Session Management By using Cookies:
---------------------------------------

Cookie is a very small amount of information created by Server and maintained by client[Browser].


Whenever client sends a request to the server,if server wants to remember client 
information for the future purpose then server will create cookie object with the required information. 

Server will send that Cookie object to the client as the part of response. 

Client will save that cookie in its local machine and send to the server with every 
consecutive request. By accessing cookies from the request server can remember client 
information.








