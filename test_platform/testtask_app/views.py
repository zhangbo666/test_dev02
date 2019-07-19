from django.shortcuts import render

from project_app.models import Project

from module_app.models import Module

from testcase_app.models import TestCase

from testtask_app.models import TestTask

from testtask_app.models import TestResult

from django.http import JsonResponse,HttpResponseRedirect

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

import json

from test_platform import settings

import os

from django.contrib.auth.decorators import login_required

from testtask_app.extend.task_thread import TaskThread



'''任务list'''
@login_required
def testtask_manage(request):

    '''任务list'''

    tasks = TestTask.objects.all()

    paginator = Paginator(tasks,2)

    # 最大分几页数字表示
    paginator_num_pages = paginator.num_pages

    # 分几页表示range(1, 3)，循环顺序1，2
    paginator_num_pages_array_ = paginator.page_range

    # 当前第一页表示<Page 1 of 2>
    # 当前第二页表示<Page 2 of 2>
    page1 = paginator.page(1)

    # 第一页编号
    page_num = page1.number

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

    return render(request,"task_list.html",{"type":"list",
                                            "tasks":contacts,
                                            "page":page,
                                            "page_num":page_num,
                                            "paginator_num_pages":paginator_num_pages,
                                            "paginator_num_pages_array_":paginator_num_pages_array_})


'''创建任务'''
@login_required
def add_task(request):

    '''创建任务'''

    return render(request,"task_add.html",{"type":"add"})


'''编辑任务'''
@login_required
def edit_task(request,tid):

    '''编辑任务'''

    return render(request,"task_edit.html",{"type":"edit"})


'''删除任务'''
@login_required
def delete_task(request,tid):

    '''删除任务'''

    if request.method == "GET":

        task = TestTask.objects.get(id=tid)

        task.delete()

        return HttpResponseRedirect("/testtask/")


'''保存任务'''
@login_required
def save_task(request):

    '''保存任务'''

    if request.method == "POST":

        name = request.POST.get("name","")
        desc = request.POST.get("desc","")
        cases = request.POST.get("cases","")
        task_id  = request.POST.get("task_id","")

        print ("任务名称&描述：",name,desc)
        print ("任务用例：",cases)
        print ("任务id：",task_id)

        # 字符串转list
        # casesList = json.loads(cases)
        # print ("casesList：",type(casesList))

        if name == "" or cases == "[]":

            return JsonResponse({"status":10102,"message":"参数不能为空！"})

        if task_id == "0":

            TestTask.objects.create(name=name,describe=desc,cases=cases)

        else:

            task = TestTask.objects.get(id=task_id)
            task.name = name
            task.describe = desc
            task.cases = cases
            task.save()

        return JsonResponse({"status":10200,"message":"success"})

    else:

        return JsonResponse({"status":10101,"message":"请求方法错误！"})


'''查看结果'''
@login_required
def see_log(request):

    if request.method == "POST":

        rid = request.POST.get("result_id")

        if rid == "":

            return JsonResponse({"status":10102,"message":"id不能为空"})

        r = TestResult.objects.get(id=rid)

        return JsonResponse({"status":10200,"message":"","data":r.result})

    else:

        return JsonResponse({"status":10101,"message":"请求方法错误！"})


'''运行任务'''
@login_required
def run_task(request):

    '''运行任务'''
    if request.method == "POST":

        tid = request.POST.get("task_id")

        if tid == "":

            return JsonResponse({"status":10101,"message":"task id is null"})

        tasks = TestTask.objects.all()

        for t in tasks:

            if t.status == 1:

                return JsonResponse({"status":10200,"message":"任务执行中，请稍后再试！"})

        # 修改任务状态为，执行中
        task = TestTask.objects.get(id=tid)

        task.status = 1

        task.save()

        # 通过多线程运行测试任务
        TaskThread(tid).run()

        return JsonResponse({"status":10200,"message":"任务开始执行！"})

    else:

        return JsonResponse({"status":10101,"message":"请求方法错误！"})


'''查看结果'''
@login_required
def result(request,tid):

    results = TestResult.objects.filter(task_id=tid).order_by("-name")

    return render(request,"task_result.html",{"type":"result","results":results})


'''任务搜索'''
@login_required
def testtask_search(request):

    '''任务搜索'''

    if request.method == "GET":

        search_name = request.GET.get("search_name","")

        task_search_list = TestTask.objects.filter(name__contains=search_name).order_by('id')#升序

        paginator = Paginator(task_search_list,2)

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


        if (len(task_search_list) == 0):

            return render(request,"task_list.html",{"type":"list",
                                                    "tasks":task_search_list,
                                                    "search_error":"搜索任务查询结果为空，请重新查询！！！"})

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

            return render(request,"task_list.html",{"type":"list",
                                                    "tasks":contacts,
                                                    "page":page,
                                                    "page_num":page_num,
                                                    "search_name":search_name,
                                                    "paginator_num_pages":paginator_num_pages,
                                                    "paginator_num_pages_array_":paginator_num_pages_array_})


'''获取用例树形结构'''
@login_required
def get_case_tree(request):

    '''获取用例树形结构'''

    if request.method == "GET":

        projects = Project.objects.all()

        data_list = []

        for project in projects:

            project_dict = {

                "name":project.name,
                "isParent":True

            }
            modules = Module.objects.filter(project_id=project.id)

            module_list = []

            for module in modules:

                module_dict = {

                    "name":module.name,
                    "isParent":True

                }

                cases = TestCase.objects.filter(module_id=module.id)

                case_list = []

                for case in cases:

                    case_dict = {

                        "name":case.name,
                        "isParent":False,
                        "id":case.id,
                        # "checked":True,

                    }

                    case_list.append(case_dict)

                module_dict['children']=case_list

                module_list.append(module_dict)

            project_dict['children']=module_list

            data_list.append(project_dict)

        return JsonResponse({"status":10200,"message":"success","data":data_list})

    elif request.method == "POST":

        tid = request.POST.get("tid","")

        if tid == "":

            return JsonResponse({"status":10200,"message":"任务id不能为空！"})

        task = TestTask.objects.get(id=tid)

        # 字符串转list
        caseList = json.loads(task.cases)


        task_dict = {

            "name":task.name,
            "describe":task.describe

        }

        projects = Project.objects.all()

        data_list = []

        for project in projects:

            project_dict = {

                 "name":project.name,
                 "isParent":True

            }
            modules = Module.objects.filter(project_id=project.id)

            module_list = []

            for module in modules:

                module_dict = {

                    "name":module.name,
                    "isParent":True

                }

                cases = TestCase.objects.filter(module_id=module.id)

                case_list = []

                for case in cases:

                    if case.id in caseList:

                        case_dict = {

                            "name":case.name,
                            "isParent":False,
                            "id":case.id,
                            "checked":True,

                        }

                    else:

                        case_dict = {

                            "name":case.name,
                            "isParent":False,
                            "id":case.id

                        }

                    case_list.append(case_dict)

                module_dict['children']=case_list

                module_list.append(module_dict)

            project_dict['children']=module_list

            data_list.append(project_dict)

        task_dict["case"] = data_list

        return JsonResponse({"status":10200,"message":"success","data":task_dict})
