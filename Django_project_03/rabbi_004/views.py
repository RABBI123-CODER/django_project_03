from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def rabbi_004(request):
    return render(request, 'rabbi_004.html')
