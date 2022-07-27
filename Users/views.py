from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from Users.form import StudentRegistrationForm,StudentLoginForm  
from django.shortcuts import render, redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from Users.models import *
from django.contrib import messages
from Users.utils import *
import os
import json
import sys
import re

def Register(request):
    form = StudentRegistrationForm()
    data={'form':form,}
    try:
        print(request.POST)
        if request.method == "POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email_id')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            print(first_name,last_name,username,email,password,confirm_password)
            if not re.search(r'^[a-zA-Z]+$' , first_name):
                print("inside this")
                messages.error(request,"Please enter a valid first name.")
            elif not re.search(r'^[a-zA-Z]+$' , last_name):
                print("inside that")
                messages.error(request,"Please enter a valid last name.")
            elif Student.objects.filter(username=username).exists():
                print("username exist")
                messages.error(request,"Username already exist!")
            elif Student.objects.filter(email_id=email).exists():
                messages.error(request,"Email already taken with another username!")
                print("email exist")
            elif password != confirm_password:
                messages.error(request,"Both password are not matching.")
            elif len(password)<8:
                messages.error(request,"Password must contain 8 characters.")
            else:
                # encrypted_obj=CustomEncrypt()
                # encrypted_password=encrypted_obj.encrypt(json.dumps(password))
                user = Student.objects.create(username=username, password=password, 
                                        email_id=email, firstname=first_name, lastname=last_name)
                messages.success(request,"Profile created successfully")
                print("account create")
        return render(request, 'Users/registeration.html',context=data)
    except Exception as e: 
        print(e)
        #exc_type, exc_obj, exc_tb = sys.exc_info()
        return render(request, 'Users/registeration.html',context=data)

def LoginSubmit(request):
    form=StudentLoginForm()
    data={'form':form,}
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            # decrypted_obj=CustomEncrypt()
            # decrypted_password=encrypted_obj.decrypt(json.dumps(password))
            obj=Student.objects.get(username=username,password=password)
            print(obj)
            if obj:
                name=obj.firstname+" "+obj.lastname
                obj.is_active=True
                obj.save()
                messages.success(request,"Dear "+name+", You have successfully logged in.")
            else:
                messages.error(request,"Invalid username or password!")
        return render(request, 'Users/login.html',context=data)

    except Exception as e:
        print(e)
        messages.error(request,"Invalid username or password!")
        return render(request, 'Users/login.html',context=data)


def home(request):
    print(request.user.username)
    try:
        obj=Student.objects.get(username=request.user.username)
        name=obj.firstname+" "+obj.lastname
        print(name)
        if obj.is_active:
            return render(request, 'Users/home.html',{'username':name})
        else:
            return redirect('login')
    except Exception as e: 
        print(e)
        messages.error(request,"Invalid username or password!")
        return render(request, 'Users/login.html',context=data)
def HomePage(request):
    return redirect('login')

def logout_user(request):
    obj=Student.objects.get(username=request.user.username)
    obj.is_active=False
    obj.save()
    return redirect('home')


