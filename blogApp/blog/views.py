from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('<h1> This is Blog Home </h1>')


def about(request):
    return HttpResponse('<p> This is the about Page da Madaiya</p>')
