__author__ = 'zhangbo'


from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from personal.models.project import Project


# 登录成功，默认项目管理页
@login_required
def project_manage(request):

    project_all = Project.objects.all()

    return render(request,"project.html",{"projects":project_all,"type":"list"})


# 添加项目
@login_required
def add_project(request):

    return render(request,"project.html",{"type":"add"})
