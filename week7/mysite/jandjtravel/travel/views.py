from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from pkg_resources import ResolutionError
# Create your views here.


def home(request):
    return render(request, 'home.html')
    
    # return render(request, 'home.html', {'name': 'Jerome'})

def add(request):
     tex1=request.GET['Firstname']
     tex2=request.GET['Lastname']
     tex3=request.GET['Phone']
     tex4=request.GET['Email']
     result = " Firstname: "  + tex1 + " LastName: " + tex2 + " Phone: " + tex3 + " Email: " + tex4
     

# def res(request):
     return render(request, 'result.html', {'result':result})