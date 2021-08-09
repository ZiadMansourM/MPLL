from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def home(request):
    #return HttpResponse('<h1> Hello world from home page </h1>')
    return render(request,'main/home.html',{
        'title':'home'
    })

def about(request):
    #return HttpResponse("<h1> Hello world from about page </h1>")    
    return render(request,'main/about.html')