from django.shortcuts import render

from project_app.models import Project

from module_app.models import Module

from testcase_app.models import TestCase

from django.http import JsonResponse

import json


# Create your views here.


def testtask_manage(request):

    '''任务管理'''

    return render(request,"task_list.html",{"type":"list"})



def add_task(request):

    '''创建任务'''

    return render(request,"task_add.html",{"type":"add"})


def save_task(request):

    '''保存任务'''

    if request.method == "POST":

        name = request.POST.get("name","")
        desc = request.POST.get("desc","")
        cases = request.POST.get("cases","")

        print ("任务名称&描述：",name,desc)
        print ("任务用例：",cases)

        # casesList = json.loads(cases)
        # print (type(casesList))

        if name == "" or cases == "[]":

            return JsonResponse({"status":10102,"message":"参数不能为空！"})


        return JsonResponse({"status":10200,"message":"success"})

    else:

        return JsonResponse({"status":10101,"message":"请求方法错误！"})


def get_case_tree(request):

    '''获取用例树'''

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
                        "id":case.id

                    }

                    case_list.append(case_dict)

                module_dict['children']=case_list

                module_list.append(module_dict)

            project_dict['children']=module_list

            data_list.append(project_dict)

        return JsonResponse({"status":10200,"message":"success","data":data_list})

