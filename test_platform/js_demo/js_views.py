from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):

    return render(request,"js_demo.html")


def js_jisuan(request):

    if request.method == "POST":

        n1 = request.POST.get("num1")

        n2 = request.POST.get("num2")

        return HttpResponse(int(n1)+int(n2))
