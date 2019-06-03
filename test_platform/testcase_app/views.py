#!/usr/bin/python
#encoding:utf-8


from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger



from testcase_app.models import TestCase
from module_app.models import Module
from project_app.models import Project

from django.contrib import messages
import requests

import json



# Create your views here.



# 用例管理

@login_required
def testcase_manage(request):

    '''测试用例管理列表页'''

    case_list = TestCase.objects.all()

    paginator = Paginator(case_list,2)

    # 多少条数据
    # paginator_count = paginator.count
    # print ("共有：",str(paginator_count)+"条数据")

    # 最大分几页数字表示
    paginator_num_pages = paginator.num_pages
    print ("共分：",str(paginator_num_pages)+"页")

    # 分几页表示range(1, 3)，循环顺序1，2
    paginator_num_pages_array_ = paginator.page_range
    print ("数组形式表示：",paginator_num_pages_array_)

    # for p1 in paginator_num_pages_array_:

        # print (p1)

    # 当前第一页表示<Page 1 of 2>
    # 当前第二页表示<Page 2 of 2>
    page1 = paginator.page(1)
    print ("第一页：",page1)

    page_num = page1.number
    print ("第一页：",page_num)

    # 当前页对象
    # page_object_list = page1.object_list
    # print (page_object_list)

    # 当前页第一条数据索引
    # print (page1.start_index())
    #
    # 当前页最后一条数据索引
    # print (page1.end_index())
    #
    # 当前页是否有上一页
    # print(page1.has_previous())
    #
    # 当前页是否有下一页
    # print(page1.has_next())
    #
    # 当前页是否有其它页
    # print (page1.has_other_pages())
    #
    # 上一页是第几页
    # print (page1.previous_page_number())
    #
    # 下一页是第几页
    # print (page1.next_page_number())
    #
    #
    #
    # for p in page1:
    #
    #     print (p.name)
    #

    # 传一个页面数据get参数的值
    page = request.GET.get('page','')
    print ("urlpage传参：",page)


    try:

        # 获取page参数的值
        contacts = paginator.page(page)
        print ("contacts---------->1",contacts)

    except PageNotAnInteger:

        contacts = paginator.page(1)

        print ("contacts---------->2",contacts)

    except EmptyPage:

        contacts = paginator.page(paginator.num_pages)

        print ("contacts---------->3",contacts)

    print ("第二页索引：",contacts.number)

    print ("第几页：",contacts)
    return render(request,"case_list.html",{"cases":contacts,
                                            "page":page,
                                            "page_num":page_num,
                                            "paginator_num_pages":paginator_num_pages,
                                            "paginator_num_pages_array_":paginator_num_pages_array_})



@login_required
def add_case(request):

    '''测试用例添加页'''

    return render(request,"case_add.html")


@login_required
def edit_case(request,cid):

    '''测试用例修改页'''

    return render(request,"case_edit.html")


@login_required
def delete_case(request,cid):

    '''测试用例删除'''

    if request.method == "GET":

        try:

            cases = TestCase.objects.get(id=cid)

            cases.delete()

        except TestCase.DoesNotExist:

            return HttpResponseRedirect("/testcase/")

        return HttpResponseRedirect("/testcase/")

    else:

        return HttpResponseRedirect("/testcase/")


@login_required
def testcase_search(request):

    '''测试用例搜索'''

    if request.method == "GET":

        search_name = request.GET.get("search_name","")

        case_search_list = TestCase.objects.filter(name__contains=search_name).order_by('id')#升序

        paginator = Paginator(case_search_list,2)

        # 最大分几页数字表示
        paginator_num_pages = paginator.num_pages
        print ("共分：",str(paginator_num_pages)+"页")


        # 分几页表示range(1, 3)，循环顺序1，2
        paginator_num_pages_array_ = paginator.page_range
        print ("数组形式表示：",paginator_num_pages_array_)

        # 当前第一页表示<Page 1 of 3>
        # 当前第二页表示<Page 2 of 3>
        # 当前第三页表示<Page 3 of 3>

        page1 = paginator.page(1)
        print ("第一页：",page1)

        page_num = page1.number
        print ("第一页：",page_num)


        if (len(case_search_list) == 0):

            return render(request,"case_list.html",{"cases":case_search_list,
                                                    "search_error":"搜索用例查询结果为空，请重新查询！！！"})

        else:

            # 传一个页面数据get参数的值
            page = request.GET.get('page','')
            print (page)

            try:

                # 获取page参数的值
                contacts = paginator.page(page)
                print ("contacts---------->1",contacts)

            except PageNotAnInteger:

                contacts = paginator.page(1)

                print ("contacts---------->2",contacts)

            except EmptyPage:

                contacts = paginator.page(paginator.num_pages)

                print ("contacts---------->3",contacts)

            return render(request,"case_list.html",{"cases":contacts,
                                                    "page":page,
                                                    "page_num":page_num,
                                                    "search_name":search_name,
                                                    "paginator_num_pages":paginator_num_pages,
                                                    "paginator_num_pages_array_":paginator_num_pages_array_})

@login_required
def testcase_debug(request):

    '''测试用例发送请求'''

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


@login_required
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



@login_required
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

        sub_type = request.POST.get("sub_type","")
        cid = request.POST.get("cid","")

        # print (method)
        # print (url)
        # print (header)
        # print (type_)
        # print (parameter)
        # print (assert_text)
        # print (assert_type)
        # print (case_name)
        # print ("module_id:",module_id)


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

        # 创建用例
        if sub_type == "1":

            TestCase.objects.create(method=method_number,url=url,header=header,
                                    parameter_type=type_number,parameter_body=parameter,
                                    assert_text=assert_text,
                                    assert_type=assert_type_number,
                                    name=case_name,module_id=module_id)


            return JsonResponse({"message":"保存成功","status":10200})

        # 修改用例
        elif sub_type == "2":

            cases = TestCase.objects.get(id=cid)

            cases.method = method_number
            cases.url = url
            cases.header = header
            cases.parameter_type = type_number
            cases.parameter_body = parameter
            cases.assert_text = assert_text
            cases.assert_type = assert_type_number
            cases.name = case_name
            cases.module_id = module_id

            cases.save()

            return JsonResponse({"message":"修改成功","status":10200})

    else:

        return JsonResponse({"message":"请求request方法错误","status":10104})


@login_required
# 获取用例数据
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


@login_required
# 获取项目和模块数据
def get_select_data(request):

    '''

    获取“项目>模块”列表

    '''

    if request.method == "GET":

        projects = Project.objects.all()

        data_list = []

        for project in projects:

            project_dict = {

                "id":project.id,
                "name":project.name,
            }

            modules = Module.objects.filter(project_id=project.id)

            module_list = []

            for module in modules:

                module_list.append({

                    "id":module.id,
                    "name":module.name,
                })

            project_dict["moduleList"] = module_list
            data_list.append(project_dict)

        return JsonResponse({"status":10200,"message":"success","data":data_list})

    else:

        return JsonResponse({"status":10100,"message":"请求方法错误"})





















