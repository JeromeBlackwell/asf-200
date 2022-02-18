from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from pkg_resources import ResolutionError
# Create your views here.


def home(request):
    # return render(request, 'home.html')
    
    return render (request, 'home.html', {'name': 'Jerome'})

def add(request):
     tex1 = int(request.Get['Firstname'])
     tex2 = int(request.Get['Lastname'])
     tex3 = int(request.Get['Phone'])
     tex4 = int(request.Get['Email'])
     result = [[' Firstname: '  + tex1 + ' LastName: ' + tex2 + ' Phone: ' + tex3 + ' Email: ' + tex4]]
     

# def res(request):
     return render(request, "result.html", {"result":result})

def add(request):
     tex1 = int(request.POST['Firstname'])
     tex2 = int(request.POST['Lastname'])
     tex3 = int(request.POST['Phone'])
     tex4 = int(request.POST['Email'])
     result = [[' Firstname: '  + tex1 + ' LastName: ' + tex2 + ' Phone: ' + tex3 + ' Email: ' + tex4]]
     

# def res(request):
     return render(request, "result.html", {"result":result})