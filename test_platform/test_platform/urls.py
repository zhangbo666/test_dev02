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
from django.urls import path

# from personal.views import say_hello
from personal.views import login_views
from personal.views import project_views
from personal.views import module_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', login_views.say_hello),
    path('index/', login_views.index),
    path('', login_views.index),
    # path('login_action/',login_views.login_action),
    path('logout/', login_views.logout),
    path('accounts/login/',login_views.index),

    # project管理
    path('project/',project_views.project_manage),
    path('project/add_project/',project_views.add_project),

    # module管理
    path('module/',module_views.moduel_manage),








]
