#!/usr/bin/python
#encoding:utf-8


from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

from testcase_app.models import TestCase
from module_app.models import Module

import requests

import json



# Create your views here.



# 用例管理
def testcase_manage(request):

    '''测试用例管理列表页'''

    case_list = TestCase.objects.all()

    return render(request,"case_list.html",{"cases":case_list})


def add_case(request):

    '''测试用例添加页'''

    return render(request,"case_add.html")


def edit_case(request,cid):

    '''测试用例修改页'''

    return render(request,"case_edit.html")


def delete_case(request):

    '''测试用例删除'''

    return render(request,"case_list.html")


def testcase_debug(request):

    '''测试用例调试'''

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

                    return JsonResponse({"result":"URL地址请求错误，请查看原因_1！！！"})

            else:

                r = requests.get(url,params=parameter,headers=header)

                try:

                    print ("结果",r.json())

                except ValueError:

                    return JsonResponse({"result":"URL地址请求错误，请查看原因_2！！！"})

            return JsonResponse({"result":r.text})

        elif method == "post":

            if type_ == "form":

                if header == "":

                    r = requests.post(url, data=parameter)

                    try:

                        print ("结果",r.json())

                    except ValueError:

                        return JsonResponse({"result":"URL地址请求错误，请查看原因_3！！！"})

                else:

                    r = requests.post(url, data=parameter,headers=header)

                    try:

                        print ("结果",r.json())

                    except ValueError:

                        return JsonResponse({"result":"URL地址请求错误，请查看原因_4！！！"})

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

    '''测试用例断言'''

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

# post:
# http://httpbin.org/post
# {"key1":"value1","key2":"value2"}

# get:
# http://httpbin.org/get
# {"key":"value"}

# json:
# https://api.github.com/some/endpoint
# {'some':'data'}

# headers
# {'user-agent':'my-app/0.0.1'}

# post:
# http://127.0.0.1:8000/js_jisuan/
# {"num1":1,"num2":'12'}




def testcase_save(request):

    '''测试用例保存'''

    if request.method == "POST":

        method    = request.POST.get("method","")
        url       = request.POST.get("url","")
        header    = request.POST.get("header","")
        type_     = request.POST.get("type","")
        parameter = request.POST.get("parameter","")

        assert_text = request.POST.get("assert","")
        assert_type = request.POST.get("assert_type","")

        case_name = request.POST.get("name","")
        module_id = request.POST.get("mid","")

        # print (method)
        # print (url)
        # print (header)
        # print (type_)
        # print (parameter)
        # print (assert_text)
        # print (assert_type)
        # print (case_name)
        print ("module_id:",module_id)


        # 请求方法判断
        if method == "get":

            method_number = 1

        elif method == "post":

            method_number = 2

        elif method == "put":

            method_number = 3

        elif method == "delete":

            method_number = 4

        else:

            return JsonResponse({"message":"请求方法错误","status":10101})

        # 请求类型判断
        if type_ == "form":

            type_number = 1

        elif type_ == "json":

            type_number =2

        else:

            return JsonResponse({"message":"请求参数类型错误","status":10102})

        # 断言类型判断
        if assert_type == "contains":

            assert_type_number = 1

        elif assert_type == "mathches":

            assert_type_number = 2

        else:

            return JsonResponse({"message":"断言类型错误","status":10103})


        TestCase.objects.create(method=method_number,url=url,header=header,
                                parameter_type=type_number,parameter_body=parameter,
                                assert_text=assert_text,
                                assert_type=assert_type_number,
                                name=case_name,module_id=module_id)


        return JsonResponse({"message":"请求成功","status":10200})

    else:

        return JsonResponse({"message":"请求request方法错误","status":10104})


def get_case_info(request):


    """获取接口数据"""

    if request.method == "POST":

        cid = request.POST.get("cid","")

        case = TestCase.objects.get(id=cid)

        module = Module.objects.get(id=case.module.id)

        project_id = module.project.id;

        case_dict = {

            "id":case.id,
            "url":case.url,
            "name":case.name,
            "method":case.method,
            "header":case.header,
            "parameter_type":case.parameter_type,
            "parameter_body":case.parameter_body,
            "assert_text":case.assert_text,
            "assert_type":case.assert_type,
            "module_id":case.module.id,
            "project_id":project_id,

        }

        return JsonResponse({"status":10200,"message":"请求成功","data":case_dict})

    else:

        return JsonResponse({"status":10100,"message":"请求方法错误"})

















