from django.shortcuts import render, HttpResponseRedirect
from .forms import UserLoginForm, UserRegisterForm

from django.contrib import auth
from django.urls import reverse


# Create your views here.

def login(request):
    flag = False
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
        else:
            flag = True
    else:
        form = UserLoginForm()



    context = {'form': form, 'flag': flag}
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        data = request.POST
        form = UserRegisterForm(data)
        print(data)
        if form.is_valid():
            form.save()
            print('ok')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)