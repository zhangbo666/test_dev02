from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

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

    return render(request,"index_1.html")


def login_action(request):

    '''
    处理登录请求
    :param request: 
    :return: 
    '''

    username = request.GET.get("username","")
    password = request.GET.get("password","")

    if username == "" or password == "":

        # print (username)
        # print (password)

        # return HttpResponse("用户名或密码为空")

        return render(request,"index_1.html",{"error":"用户名或密码为空！！！"})

    if username == "admin" and password == "123456":

        return HttpResponse("登录成功！！！")

    else:

        return render(request,"index_1.html",{"error":"用户名或密码错误！！！"})



