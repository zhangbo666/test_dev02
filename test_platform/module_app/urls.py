

from django.urls import path

from module_app import views


urlpatterns = [

    path('' ,views.moduel_manage),
    path('add_module/' ,views.add_module),
    path('edit_module/<int:mid>/', views.edit_module),
    path('delete_module/<int:mid>/', views.delete_module),
    path('search',views.module_search),

    # 接口
    path('get_module_list/',views.get_module_list),
]