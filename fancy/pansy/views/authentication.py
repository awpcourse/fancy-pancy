from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from pansy.forms.authentication import UserSigninForm, UserSignupForm
from django.contrib.auth.models import User


def signin(request):
    if request.method == 'GET':
        form = UserSigninForm()
        context = {'form': form}
        return render(request, 'signin.html', context)
    elif request.method == 'POST':
        form = UserSigninForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            context = {
                'form': form,
                'message': 'Wrong username or password!'
            }
            return render(request, 'signin.html', context)
        else:
            login(request, user)
            return redirect('/')


def signout(request):
    logout(request)
    return redirect('/signin/')


def signup(request):
    if request.method == 'GET':
        form = UserSignupForm()
        context = {'form': form}
        return render(request, 'signup.html', context)
    elif request.method == 'POST':
        form = UserSignupForm(request.POST)
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, first_name=first_name,
                                        last_name=last_name, email=email, password=password)
        user.save()
        return redirect('/signin/')