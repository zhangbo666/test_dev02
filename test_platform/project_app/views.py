#!/usr/bin/python
#encoding:utf-8


__author__ = 'zhangbo'

from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from project_app.models import Project

from datetime import datetime

from project_app.forms import ProjectForm



# 登录成功，默认项目管理页
@login_required
def project_manage(request):

    project_all = Project.objects.all()

    return render(request,"project.html",{"projects":project_all,"type":"list"})


# 添加项目
@login_required
def add_project(request):

    if request.method == 'GET':

        return render(request,"project.html",{"type":"add"})

    elif request.method == 'POST':

        project_name = request.POST.get("project_name","")

        project_describe = request.POST.get("project_describe","")

        status = request.POST.get("status","")

        if project_name == "":

            return render(request,"project.html",{"type":"add","name_error":"项目名称不能为空"})

        else:

            Project.objects.create(name=project_name,describe=project_describe,status=status,
                                   create_time=datetime(2019,4,3,00,10,00))

            return HttpResponseRedirect("/project/")


# 编辑项目
@login_required
def edit_project(request,pid):

    if request.method == 'GET':

        if pid :

            pro = Project.objects.get(id=pid)

            form = ProjectForm(instance=pro)

            return render(request,"project.html",{"type":"edit","form":form,"pid":pid})

    elif request.method == 'POST':

         form = ProjectForm(request.POST)

         if form.is_valid():

             name = form.cleaned_data['name']

             describe = form.cleaned_data['describe']

             status   = form.cleaned_data['status']

             p_update = Project.objects.get(id=pid)

             p_update.name = name

             p_update.describe = describe

             p_update.status = status

             p_update.save()

             return HttpResponseRedirect("/project/")


# 删除项目
@login_required
def delete_project(request,pid):

    if request.method == "GET":

        try:

            project = Project.objects.get(id=pid)

            project.delete()

        except Project.DoesNotExist:

            return HttpResponseRedirect("/project/")

        return HttpResponseRedirect("/project/")

    else:

        return HttpResponseRedirect("/project/")


# 接口：获取项目list_info数据
@login_required
def get_project_list(request):

    if request.method == "GET":

        projects = Project.objects.all()

        project_list = []
        # project_dict = {}

        for pro in projects:

            # project_list.append(pro.name)
            # project_dict[pro.id] = pro.name

            project_dict = {

                "id":pro.id,
                "name":pro.name
            }

            project_list.append(project_dict)

        print (project_list)

        return JsonResponse({"status":10200,"data":project_list,"message":"请求成功",})

    else:

        return JsonResponse({"status":10101,"message":"请求方法错误"})