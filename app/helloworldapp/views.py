from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def helloworldappview(request):
    return HttpResponse('<h1>でかした！！</h1>')