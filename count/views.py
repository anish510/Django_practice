from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def index(request):
    return render(request, 'index.html')

def counter(request):
    texts = request.GET['texts']
    total_count = len(texts.split())
    return render (request, 'counter.html',{'words': total_count})
