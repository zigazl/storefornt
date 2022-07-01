from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    #pull data from db
    #transform data
    #send email
    #return HttpResponse("Hello, world!") #returns a response
    return render(request, "hello.html", {"name": "Ziga"}) #returns a response
    
