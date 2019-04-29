#!/usr/bin/python
#encoding:utf-8


from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

import requests

import json



# Create your views here.



# 用例管理
def testcase_manage(request):

    return render(request,"testcase.html",{"type":"debug"})


def testcase_debug(request):

    '''测试用例的调试'''
    print (request.method)

    if request.method == "POST":

        method    = request.POST.get("method","")
        url       = request.POST.get("url","")
        header    = request.POST.get("header","")
        type_     = request.POST.get("type","")
        parameter = request.POST.get("parameter","")

        # 判断header 是否为数字型
        if header.isdigit():

            return JsonResponse({"result": "headers值为数字型字符串，请更改headers传参"})

        #参数中用单引号，用字符串替换 replace()，替换单引号为双引号
        json_header = header.replace("\'","\"")

        try:

            pass

        except:

            return JsonResponse({"result": "请求的URL地址错误1！！！"})


        try:

            if header == "":

                pass

            else:

                header      = json.loads(json_header)

        except ValueError:

                return JsonResponse({"result":"headers传参数错误！！！"})


        #参数中用单引号，用字符串替换 replace()，替换单引号为双引号
        json_par  = parameter.replace("\'","\"")

        try:

            # 字符串转json串
            payload   = json.loads(json_par)

        except ValueError:

                return JsonResponse({"result":"参数类型返回错误！！！"})

        print ("payload--->",payload)
        # print ("method",method)
        # print ("url",url)
        # print ("header",header)
        # print ("type_",type_)
        # print ("parameter",parameter)

        if method == "get":

            if header == "":

                r = requests.get(url,params=payload)

                print ("结果",r.json())

            else:

                r = requests.get(url,params=payload,headers=header)

                print ("结果",r.text)

            return JsonResponse({"result":r.text})

        elif method == "post":

            if type_ == "from":

                if header == "":

                    r = requests.post(url, data=payload)

                    print (r.json())

                else:

                    r = requests.post(url, data=payload,headers=header)

                    print (r.text)

            elif type_ == "json":

                if header == "":

                    r = requests.post(url, json=payload)

                    print (r.json())

                else:

                    r = requests.post(url, json=payload,headers=header)

                    print (r.text)

        return JsonResponse({"result":r.text})

    elif request.method == "GET":

        return JsonResponse({"result":"请求方法错误"})


def testcase_assert(request):

    '''测试用例的断言'''




# example

# post:http://httpbin.org/post
# {"key1":"value1","key2":"value2"}

# get:http://httpbin.org/get
# {"key":"value"}

# json:https://api.github.com/some/endpoint
# {'some':'data'}

# headers
# {'user-agent':'my-app/0.0.1'}

# http://127.0.0.1:8000/js_jisuan/
# {"num1":1,"num2":'12'}








