from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Welcome to the language learning platform ...")

# Create your views here.


def base(request):
    return render(request, 'base.html')



