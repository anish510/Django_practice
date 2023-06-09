from django.shortcuts import render
from django.http import HttpRequest
from . models import features

# Create your views here.


def index(request):
    features1 = features()
    features1.id = 0
    features1.name = 'fast'
    features1.details = 'our server is very quick'

    features2 = features()
    features2.id = 2
    features2.name = 'anish'
    features2.details = 'our server is very quick'

    features3 = features()
    features3.id = 3
    features3.name = 'joshi'
    features3.details = 'our server is very quick'

    feature = [features1, features2, features3]

    return render(request, 'index.html', {'features': feature})


def second_index(request):
    return render(request, "second_index.html")


def counter(request):
    texts = request.POST['texts']
    total_count = len(texts.split())
    return render(request, 'counter.html', {'words': total_count})
