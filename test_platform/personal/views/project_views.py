__author__ = 'zhangbo'


from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from personal.models.project import Project

import datetime

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

        print (project_name)
        print (project_describe)
        print (status)

        Project.objects.create(name=project_name,describe=project_describe,status=status,
                               create_time=datetime(2019,04,02,19,50,00))


        # return render(request,"project.html",{"type":"add"})

