from django.shortcuts import render
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
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')
