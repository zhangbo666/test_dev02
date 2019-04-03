__author__ = 'zhangbo'

from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from personal.models.project import Project

from datetime import datetime

from personal.forms import ProjectForm



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


