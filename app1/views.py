from django.shortcuts import render
from django.views.generic import View


# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def mobin(request):
    return render(request,'mobin.html')

def rafi(request):
    return render(request,'rafi.html')