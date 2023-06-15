from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return HttpResponse('Hello, World')
def Chmi_Ele(request):
    return HttpResponse('ELEs')
def great(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")

def ran(request):
    return render(request, "hello/ran.html")