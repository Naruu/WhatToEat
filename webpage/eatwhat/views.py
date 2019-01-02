from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(result) :
    return HttpResponse("index.html")