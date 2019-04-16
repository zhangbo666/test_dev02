from django.shortcuts import render

from django.http import HttpResponse

from django.http import JsonResponse


# Create your views here.


def index(request):

    return render(request,"js_demo.html")


def js_jisuan(request):

    if request.method == "POST":

        n1 = request.POST.get("num1","")

        n2 = request.POST.get("num2","")

        if n1 == "" or n2 == "":

            return JsonResponse({"status_code":1001,"message":"参数为空！！！"})

        else:

            try:

                n1 = int(n1)

                n2 = int(n2)

            except ValueError:

                return JsonResponse({"status_code": 1003, "message": "参数类型错误！！！"})

            return JsonResponse({"status_code":200,"message":"请求接口正确！！！","data":n1+n2 })

    elif request.method == "GET":

            return JsonResponse({"status_code":1002,"message":"请求方法错误！！！"})
