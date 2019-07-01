from django.shortcuts import render

from project_app.models import Project

from module_app.models import Module

from testcase_app.models import TestCase

from testtask_app.models import TestTask

from django.http import JsonResponse,HttpResponseRedirect

import json

from test_platform import settings

import unittest

import xmlrunner

import os


'''任务list'''
def testtask_manage(request):

    '''任务list'''

    tasks = TestTask.objects.all()

    return render(request,"task_list.html",{"type":"list","tasks":tasks})


'''创建任务'''
def add_task(request):

    '''创建任务'''

    return render(request,"task_add.html",{"type":"add"})


'''编辑任务'''
def edit_task(request,tid):

    '''编辑任务'''

    return render(request,"task_edit.html",{"type":"edit"})


'''删除任务'''
def delete_task(request,tid):

    '''删除任务'''

    if request.method == "GET":

        task = TestTask.objects.get(id=tid)

        task.delete()

        return HttpResponseRedirect("/testtask/")


'''保存任务'''
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

'''运行任务'''
def run_task(request):

    '''运行任务'''
    if request.method == "POST":

        tid = request.POST.get("task_id")

        if tid == "":

            return JsonResponse({"status":10101,"message":"task id is null"})

        task = TestTask.objects.get(id=tid)

        print (task.cases)
        print (type(task.cases))

        case_list = json.loads(task.cases)
        print (type(case_list))

        test_data = {}
        for cid in case_list:

            case = TestCase.objects.get(id=cid)

            if case.method == 1:

                method = "get"

            elif case.method == 2:

                method = "post"

            if case.parameter_type == 1:

                parameter_type = "from"

            elif case.parameter_type == 2:

                parameter_type = "json"

            if case.assert_type == 1:

                assert_type = "contains"

            elif case.assert_type == 2:

                assert_type = "mathches"

            test_data[case.id] = {

                "url":case.url,
                "method":method,
                "header":case.header,
                "parameter_type":parameter_type,
                "parameter_body":case.parameter_body,
                "assert_type":assert_type,
                "assert_text":case.assert_text,

            }
        print ("任务下面的用例：",json.dumps(test_data))
        case_data = json.dumps(test_data)

        BASE_PATH = settings.BASE_DIR + "/testtask_app/extend/"
        with(open(BASE_PATH + "test_data_list.json","w"))as f:

            f.write(case_data)

        run_cmd = "pytest -vs " + BASE_PATH + "run_task.py --junitxml="+BASE_PATH+"result.html"
        # print ("运行的命令",run_cmd)

        os.system("pytest -vs " + BASE_PATH + "run_task.py --junitxml="+BASE_PATH+"result.html")

        return JsonResponse({"status":10200,"message":"任务执行完成！"})


    else:

        return JsonResponse({"status":10101,"message":"请求方法错误！"})




'''获取用例树形结构'''
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
