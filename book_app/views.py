from django.shortcuts import render,HttpResponse

# Create your views here.
def login(request):
    return HttpResponse("login")

def reg(request):
    return HttpResponse("reg")

def add(request):
    return HttpResponse("add")

def clear(request):
    return HttpResponse("clear")