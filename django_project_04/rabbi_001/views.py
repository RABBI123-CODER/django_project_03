from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def rabbi_0001(request):
    return render(request, 'rabbi_001/rabbi_001.html')


def rabbi_0002(request):
    return render(request, 'rabbi_001/rabbi_002.html')


def rabbi_0003(request):
    return render(request, 'rabbi_001/rabbi_003.html')


def rabbi_0004(request):
    return render(request, 'rabbi_001/rabbi_004.html')
