from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm


def home(request):
    return render(request, 'list_task/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(
            request,
            'list_task/signupuser.html',
            {'form': UserCreationForm()}
        )
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'list_task/signupuser.html', {'form': UserCreationForm(),  'error': 'Username has already been taken'})

        else:
            return render(request, 'list_task/signupuser.html', {'form': UserCreationForm(),  'error': 'Password did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(
            request,
            'list_task/loginuser.html',
            {'form': AuthenticationForm()}
        )
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'list_task/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username or password did not match'}
                          )
        else:
            login(request, user)
            return redirect('currenttodos')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def currenttodos(request):
    return render(request, 'list_task/currenttodos.html')


def createtodo(request):
    if request.method == 'GET':
        return render(request, 'list_task/createtodo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'list_task/createtodo.html', {'form': TodoForm(), 'error': "Bad data passed in"})
