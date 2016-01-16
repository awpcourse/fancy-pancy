from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from pansy.forms.authentication import UserSigninForm, UserSignupForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def signin(request):
    if request.method == 'GET':
        form = UserSigninForm()
        context = {'form': form}
        return render(request, 'signin.html', context)
    elif request.method == 'POST':
        form = UserSigninForm(request.POST)

        if not form.is_valid():
            context={'form': form}
            return render(request, 'signin.html', context)

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
        if not form.is_valid():
            context = {'form': form}
            return render(request, 'signup.html', context)
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        password1 = request.POST['retype_password']

        if not password1:
            raise ValidationError("You must confirm your password")
        if password != password1:
            raise ValidationError("Your passwords do not match")

        user = User.objects.create_user(username=username, first_name=first_name,
                                        last_name=last_name, email=email, password=password)
        user.save()
        return redirect('/signin/')