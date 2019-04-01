__author__ = 'zhangbo'


from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from personal.models.module import Module




# 模块管理页
@login_required
def moduel_manage(request):

    module_all = Module.objects.all()

    return render(request,"module.html",{"modules":module_all})