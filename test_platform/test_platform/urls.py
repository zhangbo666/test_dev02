"""test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# from personal.views import say_hello
from user_app import views

from js_demo import js_views


urlpatterns = [

    # 练习
    # path('hello/', views.say_hello),
    # path('login_action/',views.login_action),

    # admin后台
    path('admin/', admin.site.urls),

    # 用户应用
    path('', views.index),
    path('index/', views.index),
    path('accounts/login/', views.index),

    # 用户应用退出登录
    path('logout/', views.logout),

    # 项目管理
    path('project/',include('project_app.urls')),
    # path('project/',project_views.project_manage),
    # path('project/add_project/',project_views.add_project),
    # path('project/edit_project/<int:pid>/',project_views.edit_project),
    # path('project/delete_project/<int:pid>/',project_views.delete_project),

    # 模块管理
    path('module/', include('module_app.urls')),
    # path('module/',module_views.moduel_manage),
    # path('module/add_module/',module_views.add_module),
    # path('module/edit_module/<int:mid>/', module_views.edit_module),
    # path('module/delete_module/<int:mid>/', module_views.delete_module),

    # 用例管理
    path('testcase/', include('testcase_app.urls')),

    # js例子
    path('js/',js_views.index),
    path('js_jisuan/',js_views.js_jisuan),








]
