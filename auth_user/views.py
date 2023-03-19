from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import RegisterUserForm


# Create your views here


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(
                reverse('climate:home')
            )
        else:
            messages.success(request, "There was an error in Logging in. Try again...")
            return HttpResponseRedirect(
                reverse('auth_user:login')
            )
    else:
        return render(request, 'authentication/login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(
            reverse('climate:home')
        )


def registration(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            password = form.cleaned_data['password1']
            username = form.cleaned_data['username']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successful!")
            return redirect('climate:home')
    else:
        form = RegisterUserForm()
    return render(request, 'authentication/registration.html', {'form': form,})