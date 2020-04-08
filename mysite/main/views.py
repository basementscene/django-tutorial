from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>Hello world wide web!</h1>")

def view_1(response):
    return HttpResponse("First view test.")