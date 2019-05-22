__author__ = 'zhangbo'


from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from module_app.models import Module

from project_app.models import Project

from django.http import HttpResponseRedirect,JsonResponse

from module_app.forms import ModuleForm


# 模块管理页
@login_required
def moduel_manage(request):

    if request.method == "GET":

        module_all = Module.objects.all()

        return render(request,"module.html",{"modules":module_all,"type":"list"})


# 添加模块
@login_required
def add_module(request):

    '''第一种方式：html的form表单'''
    '''
    project_all = Project.objects.all()

    if request.method == 'GET':

        return render(request,"module.html",{"projects":project_all,"type":"add"})

    elif request.method == 'POST':

        module_name = request.POST.get("module_name","")

        module_describe = request.POST.get("module_describe","")

        module_project = request.POST.get("module_project","")

        project_name = Project.objects.get(name=module_project)

        project_id   = project_name.id


        if module_name == "":

            return render(request,"module.html",{"type":"add","projects":project_all,"name_error":"模块名称不能为空"})

        else:

            Module.objects.create(name=module_name,describe=module_describe,project_id=project_id)

            return HttpResponseRedirect("/module/")
    '''


    '''第二种方式：django的form表单'''
    if request.method == "GET":

        module_form = ModuleForm()

        return render(request, "module.html", {"form": module_form, "type": "add"})


    else:

        form = ModuleForm(request.POST)

        if form.is_valid():

            project = form.cleaned_data['project']

            name = form.cleaned_data['name']

            describe = form.cleaned_data['describe']

            Module.objects.create(name=name, describe=describe, project=project)

            return HttpResponseRedirect("/module/")


# 编辑模块
@login_required
def edit_module(request,mid):

    if request.method == 'GET':

        if mid :

            pro = Module.objects.get(id=mid)

            form = ModuleForm(instance=pro)

            return render(request,"module.html",{"type":"edit","form":form,"mid":mid})

    elif request.method == 'POST':

         form = ModuleForm(request.POST)

         if form.is_valid():

             project = form.cleaned_data['project']

             name = form.cleaned_data['name']

             describe = form.cleaned_data['describe']

             m_update = Module.objects.get(id=mid)

             m_update.project = project

             m_update.name = name

             m_update.describe = describe

             m_update.save()

             return HttpResponseRedirect("/module/")


# 删除模块
@login_required
def delete_module(request,mid):

    if request.method == "GET":

        try:

            module = Module.objects.get(id=mid)

            module.delete()

        except Module.DoesNotExist:

            return HttpResponseRedirect("/module/")

        return HttpResponseRedirect("/module/")

    else:

        return HttpResponseRedirect("/module/")


# 接口：获取模块list_info数据
@login_required
def get_module_list(request):

    if request.method == "POST":

        pid = request.POST.get("pid","")

        if pid == "":

            return JsonResponse({"status":10102,"message":"项目id不能为空"})

        modules = Module.objects.filter(project=pid)

        modules_list = []

        for mod in modules:

            modules_dict = {

                "id":mod.id,
                "name":mod.name,
            }

            modules_list.append(modules_dict)

        return JsonResponse({"status":10200,"message":"请求成功","data":modules_list})

    else:

        return JsonResponse({"status":10101,"message":"请求方法错误"})