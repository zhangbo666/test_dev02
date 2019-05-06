
from django.urls import path

from project_app import views


urlpatterns = [

    path('',views.project_manage),
    path('add_project/',views.add_project),
    path('edit_project/<int:pid>/',views.edit_project),
    path('delete_project/<int:pid>/',views.delete_project),
    path('get_project_list/',views.get_project_list),
]