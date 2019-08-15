#!/usr/bin/python
#encoding:utf-8


__author__ = 'zhangbo'

from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


from project_app.models import Project

from datetime import datetime

from project_app.forms import ProjectForm



# 登录成功，默认项目管理页
@login_required
def project_manage(request):

    project_all = Project.objects.all()

    paginator = Paginator(project_all,5)

    # 最大分几页数字表示
    paginator_num_pages = paginator.num_pages
    print ("共分：",str(paginator_num_pages)+"页")

    # 分几页表示range(1, 3)，循环顺序1，2
    paginator_num_pages_array_ = paginator.page_range
    print ("数组形式表示：",paginator_num_pages_array_)


    # 当前第一页表示<Page 1 of 2>
    # 当前第二页表示<Page 2 of 2>
    page1 = paginator.page(1)
    print ("第一页：",page1)

    page_num = page1.number
    print ("第一页：",page_num)


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


    return render(request,"project.html",{"projects":contacts,
                                          "type":"list",
                                          "page":page,
                                          "page_num":page_num,
                                          "paginator_num_pages":paginator_num_pages,
                                          "paginator_num_pages_array_":paginator_num_pages_array_})


# 添加项目
@login_required
def add_project(request):

    '''第一种方式：html的form表单'''
    
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

    '''第二种方式：django的form表单'''

    '''
    if request.method == "GET":

        project_form = ProjectForm()

        return render(request, "project.html", {"form": project_form, "type": "add"})


    else:

        form = ProjectForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']

            describe = form.cleaned_data['describe']

            status = form.cleaned_data['status']

            Project.objects.create(name=name, describe=describe, status=status)

            return HttpResponseRedirect("/project/")
    '''


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


# 项目搜索
@login_required
def project_search(request):

    '''项目搜索'''

    if request.method == "GET":

        search_name = request.GET.get("search_name","")

        project_search_list = Project.objects.filter(name__contains=search_name).order_by('id')#升序

        paginator = Paginator(project_search_list,5)

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



        if (len(project_search_list) == 0):

            return render(request,"project.html",{"projects":project_search_list,
                                                  "search_error":"搜索项目查询结果为空，请重新查询",
                                                  "type":"list"})

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


            return render(request,"project.html",{"projects":contacts,
                                                  "type":"list",
                                                  "page":page,
                                                  "page_num":page_num,
                                                  "search_name":search_name,
                                                  "paginator_num_pages":paginator_num_pages,
                                                  "paginator_num_pages_array_":paginator_num_pages_array_})


# 接口：获取项目list_info数据
@login_required
def get_project_list(request):

    if request.method == "GET":

        projects = Project.objects.all()

        project_list = []

        for pro in projects:

            project_dict = {

                "id":pro.id,
                "name":pro.name
            }

            project_list.append(project_dict)

        print (project_list)

        return JsonResponse({"status":10200,"data":project_list,"message":"请求成功",})

    else:

        return JsonResponse({"status":10101,"message":"请求方法错误"})