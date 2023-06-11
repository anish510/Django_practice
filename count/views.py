from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib import messages, auth
from django.http import HttpRequest
from . models import features


# Create your views here.


def index(request):
    feature = features.objects.all()
    return render(request, 'index.html', {'features': feature})


def second_index(request):
    return render(request, "second_index.html")


def counter(request):
    texts = request.POST['texts']
    total_count = len(texts.split())
    return render(request, 'counter.html', {'words': total_count})


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('second_index')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('second_index')


def post(request, pk):
    return render(request, 'post.html', {'pk': pk})
