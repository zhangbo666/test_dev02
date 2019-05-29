from django.urls import path
from testcase_app import views

__author__ = 'zhangbo'



urlpatterns = [

    #用例管理
    path('',views.testcase_manage),
    path('debug',views.testcase_debug),
    path('assert',views.testcase_assert),
    path('save_case',views.testcase_save),
    path('add_case/',views.add_case),
    path('edit_case/<int:cid>/',views.edit_case),
    path('delete_case/',views.delete_case),

    # 获取用例数据接口
    path('get_case_info',views.get_case_info),

    # 获取项目与模块下拉框数据接口
    path('get_select_data',views.get_select_data),



]