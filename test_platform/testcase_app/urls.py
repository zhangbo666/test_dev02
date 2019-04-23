from django.urls import path
from testcase_app import views

__author__ = 'zhangbo'



urlpatterns = [

    #用例管理
    path('',views.testcase_manage),


]