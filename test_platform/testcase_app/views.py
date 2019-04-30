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

        # 判断parameter 是否为数字型
        if parameter.isdigit():

            return JsonResponse({"result": "parameter值为数字型字符串，请更改parameter传参"})


        #参数中用单引号，用字符串替换 replace()，替换单引号为双引号
        json_header = header.replace("\'","\"")

        try:

            if header == "":

                pass

            else:

                # 字符串转json串
                header      = json.loads(json_header)

        except ValueError:

                return JsonResponse({"result":"headers传参数错误！！！"})


        #参数中用单引号，用字符串替换 replace()，替换单引号为双引号
        json_parameter  = parameter.replace("\'","\"")

        try:

            if parameter == "":

                return JsonResponse({"result":"参数数据传值为空！！！"})

            # 字符串转json串
            parameter   = json.loads(json_parameter)

        except ValueError:

                return JsonResponse({"result":"参数数据传值错误！！！"})

        # print ("parameter--->",parameter)
        # print ("method",method)
        # print ("url",url)
        # print ("header",header)
        # print ("type_",type_)
        # print ("parameter",parameter)

        if method == "get":

            if header == "":

                r = requests.get(url,params=parameter)

                try:

                    print ("结果",r.json())

                except ValueError:

                    return JsonResponse({"result":"URL地址请求错误，请查看原因！！！"})

            else:

                r = requests.get(url,params=parameter,headers=header)

                try:

                    print ("结果",r.json())

                except ValueError:

                    return JsonResponse({"result":"URL地址请求错误，请查看原因！！！"})

            return JsonResponse({"result":r.text})

        elif method == "post":

            if type_ == "from":

                if header == "":

                    r = requests.post(url, data=parameter)

                    try:

                        print ("结果",r.json())

                    except ValueError:

                        return JsonResponse({"result":"URL地址请求错误，请查看原因！！！"})

                else:

                    r = requests.post(url, data=parameter,headers=header)

                    try:

                        print ("结果",r.json())

                    except ValueError:

                        return JsonResponse({"result":"URL地址请求错误，请查看原因！！！"})

            elif type_ == "json":

                if header == "":

                    r = requests.post(url, json=parameter)

                    try:

                        print ("结果",r.json())

                    except ValueError:

                        return JsonResponse({"result":"URL地址请求错误，请查看原因！！！"})

                else:

                    r = requests.post(url, json=parameter,headers=header)

                    try:

                        print ("结果",r.json())

                    except ValueError:

                        return JsonResponse({"result":"URL地址请求错误，请查看原因！！！"})

            return JsonResponse({"result":r.text})

    elif request.method == "GET":

        return JsonResponse({"result":"请求方法错误"})


def testcase_assert(request):

    '''测试用例的断言'''

    if request.method == "POST":

        result_text = request.POST.get("result","")
        assert_text = request.POST.get("assert","")
        assert_type = request.POST.get("assert_type","")

        if result_text == "" or assert_text == "":

            return JsonResponse({"result":"断言的文本不能为空"})

        if assert_type == "contains":

            if assert_text not in result_text:

                return JsonResponse({"result": "断言失败"})

            else:

                return JsonResponse({"result": "断言成功"})

        elif assert_type == "mathches":

            if assert_text != result_text:

                return JsonResponse({"result": "断言失败"})

            else:

                return JsonResponse({"result": "断言成功"})

    else:

        return JsonResponse({"result":"请求方法错误"})


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








