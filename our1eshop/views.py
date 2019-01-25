from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def index(request):

    # return HttpResponse('Hello')
    return  render(request,'index.html')

def login(request):
    return render(request,'login.html')