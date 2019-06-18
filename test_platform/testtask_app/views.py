from django.shortcuts import render

from project_app.models import Project

from module_app.models import Module

from testcase_app.models import TestCase

from testtask_app.models import TestTask

from django.http import JsonResponse

import json


# Create your views here.


def testtask_manage(request):

    '''任务管理'''

    tasks = TestTask.objects.all()

    return render(request,"task_list.html",{"type":"list","tasks":tasks})


def add_task(request):

    '''创建任务'''

    return render(request,"task_add.html",{"type":"add"})


def edit_task(request,tid):

    '''编辑任务'''

    return render(request,"task_edit.html",{"type":"edit"})


def save_task(request):

    '''保存任务'''

    if request.method == "POST":

        name = request.POST.get("name","")
        desc = request.POST.get("desc","")
        cases = request.POST.get("cases","")
        tid  = request.POST.get("tid","")

        print ("任务名称&描述：",name,desc)
        print ("任务用例：",cases)

        # 字符串转list
        # casesList = json.loads(cases)
        # print ("casesList：",type(casesList))

        if name == "" or cases == "[]":

            return JsonResponse({"status":10102,"message":"参数不能为空！"})

        TestTask.objects.create(name=name,describe=desc,cases=cases)

        return JsonResponse({"status":10200,"message":"success"})

    else:

        return JsonResponse({"status":10101,"message":"请求方法错误！"})


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
            "describe":task.describe,

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
