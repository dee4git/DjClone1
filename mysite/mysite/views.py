from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return  HttpResponse('Working')
    return render(request, 'index.html')


def another(request):
    return render(request, 'another.html')
