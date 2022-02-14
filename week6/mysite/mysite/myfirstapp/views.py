from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from pkg_resources import ResolutionError
# Create your views here.


def home(request):
    return render(request, 'home.html', {'name': 'This is my first App in Django.  I am attempting the inevitable, by building a larger app with multiple pages and it will be an amazing app once I am do with it. As you can see, I now building a forms with a submit button below this paragragh hoping to capture data once a customer keys in their information and then it will be stored or I could even print it our for later use. Just an FYI, the Form is not completely set up yet'})
    # return render(request)

def add(request):
     tex1= request.GET['First_name']
     tex2=request.GET['Last_name']
     result = tex1 + tex2


def result(request):
    return render(request, "result.html", {'result':result})