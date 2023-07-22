from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def rabbi_001(request):
    return render(request, 'rabbi_001.html')
