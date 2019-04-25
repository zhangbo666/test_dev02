from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

import requests

import json



# Create your views here.



# 用例管理
def testcase_manage(request):

    return render(request,"testcase.html",{"type":"debug"})


def debug(request):

    print (request.method)

    if request.method == "POST":

        method    = request.POST.get("method")
        url       = request.POST.get("url")
        header    = request.POST.get("header")
        type_     = request.POST.get("type")
        parameter = request.POST.get("parameter")

        json_par  = parameter.replace("\'","\"")

        # 字符串转json串
        payload   = json.loads(json_par)



        # print ("method",method)
        # print ("url",url)
        # print ("header",header)
        # print ("type_",type_)
        # print ("parameter",parameter)

        if method == "get":

            r = requests.get(url,params=payload)

            print ("结果",r.json())

            return JsonResponse({"result":r.text})

        elif method == "post":

            if type_ == "from":

                r = requests.post(url, data=payload)

                print (r.json())

            elif type_ == "json":

                r = requests.post(url, json=payload)

                print (r.text)

            return JsonResponse({"result":r.text})

    elif request.method == "GET":

        return JsonResponse({"result":"请求方法错误"})



# {"key1":"value1","key2":"value2"}
# {"key":"value"}










