from django.shortcuts import render, HttpResponse

# Create your views here.
def testing(request):
    return HttpResponse("This is a testing page for the comments app.")