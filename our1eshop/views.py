from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def index(request):

    # return HttpResponse('Hello')
    return  render(request,'index.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        print(username,password)
    return render(request,"login.html",)

def register(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        code = request.POST.get("code",None)
        print(username,password,code)
    return render(request,"login.html",)