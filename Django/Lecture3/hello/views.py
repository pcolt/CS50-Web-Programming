from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello, World! Hello again")

def pablo(request):
	return HttpResponse("Hello, Pablo!")

def rosi(request):
	return HttpResponse("Hello, Rosi!")

def greet(request, name):
	return HttpResponse(f"Hello, {name.capitalize()}!")
