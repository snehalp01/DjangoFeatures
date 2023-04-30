from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout 
# Create your views here.

def signup(request):
    print("******request.POST ", request.POST)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else: form = UserCreationForm()
    # form = UserCreationForm()
    return render(request,"accounts/signup.html", {'form':form})
