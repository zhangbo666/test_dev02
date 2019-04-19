from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect

from django.contrib import auth

from django.contrib.auth.decorators import login_required


def say_hello(request):

    input_name = request.GET.get("name","")

    if input_name == "":

        return HttpResponse("请输入参数?name=name值")

    #第一种显示
    # talk = []
    # for n in  range(3):
    #     print ("hello," + input_name)
    #     talk.append("hello," + input_name + "<br>")

    #第二种显示
    # html = '<h1 style = "color:red">hello,' + input_name + "</h1><br>"

    #第三种显示render
    # return HttpResponse(html)

    return render(request,"index.html",{"name" : input_name})


def index(request):

    """
    登录的首页
    """

    if request.method== "GET":

       return render(request,"index_1.html")

    elif request.method == "POST":

            '''
            处理登录请求
            :param request:
            :return:
            '''

            username = request.POST.get("username","")
            password = request.POST.get("password","")

            if username == "" or password == "":

                # print (username)
                # print (password)

                # return HttpResponse("用户名或密码为空")

                return render(request,"index_1.html",{"error":"用户名或密码为空！！！"})

            userLoginInfo = auth.authenticate(username=username,password=password)

            if userLoginInfo is None:

                return render(request, "index_1.html", {"error": "用户名或密码错误！！！"})


            # if username == "admin" and password == "123456":

            else:

                # return HttpResponse("登录成功！！！")

                # return render(request, "manage.html")

                #记录用户的登录状态
                auth.login(request,userLoginInfo)

                return HttpResponseRedirect("/project/")


# 处理用户的退出
def logout(request):

    #退出登录
    auth.logout(request)

    return HttpResponseRedirect("/index/")



def login_action(request):

    '''
    处理登录请求
    :param request: 
    :return: 
    '''
    print (request.method)

    username = request.POST.get("username","")
    password = request.POST.get("password","")

    if username == "" or password == "":

        # print (username)
        # print (password)

        # return HttpResponse("用户名或密码为空")

        return render(request,"index_1.html",{"error":"用户名或密码为空！！！"})

    if username == "admin" and password == "123456":

        return HttpResponse("登录成功！！！")

    else:

        return render(request,"index_1.html",{"error":"用户名或密码错误！！！"})



