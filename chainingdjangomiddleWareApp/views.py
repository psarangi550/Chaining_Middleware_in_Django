from django.shortcuts import render,HttpResponse

# Create your views here.
def index_view(request):
    print("This code is executed bny the view function when the request response of middleware reach to the view function  ")
    return HttpResponse("<h1> Welcome to index page </h1>")
