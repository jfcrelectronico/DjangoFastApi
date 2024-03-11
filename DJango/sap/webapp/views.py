
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def mensaje1(request):
    return HttpResponse ('Mensaje JFCR Django')