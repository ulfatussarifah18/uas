from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'tahu.html')


def about(request):
    return render(request,'index.html')

    
