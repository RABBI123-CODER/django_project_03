
from django.urls import path
from . import views

urlpatterns = [
    path('fi/', views.rabbi_0001),
    path('fir/', views.rabbi_0002),
    path('firs/', views.rabbi_0003),
    path('first/', views.rabbi_0004),

]
