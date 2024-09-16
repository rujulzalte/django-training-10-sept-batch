from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# BusinessLogic/ Functionality


def homepage(request):
    # return HttpResponse("Hello World")
    return render(request, 'Login/homepage.html')


def index(request):
    return render(request, 'Login/index.html')
