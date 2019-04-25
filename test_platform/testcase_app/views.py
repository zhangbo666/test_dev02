from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

import requests

import json



# Create your views here.



# 用例管理
def testcase_manage(request):

    return render(request,"testcase.html",{"type":"debug"})


def debug(request):

    print (request.method)

    if request.method == "POST":

        method    = request.POST.get("method","")
        url       = request.POST.get("url","")
        header    = request.POST.get("header","")
        type_     = request.POST.get("type","")
        parameter = request.POST.get("parameter","")


        json_header = header.replace("\'","\"")

        try:

            header      = json.loads(json_header)

        except ValueError:

                return JsonResponse({"result":"headers传值错误"})

        # except AttributeError:

                # return JsonResponse({"result":"headers属性错误"})

        #参数中用单引号，用字符串替换 replace()，替换单引号为双引号
        json_par  = parameter.replace("\'","\"")

        try:

            # 字符串转json串
            payload   = json.loads(json_par)

        except ValueError:

                return JsonResponse({"result":"参数类型错误"})



        # print ("method",method)
        # print ("url",url)
        # print ("header",header)
        # print ("type_",type_)
        # print ("parameter",parameter)

        if method == "get":

            if header == "":

                r = requests.get(url,params=payload)

                print ("结果",r.json())

            else:

                r = requests.get(url,params=payload,headers=header)

                print ("结果",r.json())

            return JsonResponse({"result":r.text})

        elif method == "post":

            if type_ == "from":

                if header == "":

                    r = requests.post(url, data=payload)

                    print (r.json())

                else:

                    r = requests.post(url, data=payload,headers=header)

                    print (r.json())

            elif type_ == "json":

                if header == "":

                    r = requests.post(url, json=payload)

                    print (r.text)


                else:

                    r = requests.post(url, json=payload,headers=header)

                    print (r.text)

        return JsonResponse({"result":r.text})

    elif request.method == "GET":

        return JsonResponse({"result":"请求方法错误"})


# example

# post:http://httpbin.org/post
# {"key1":"value1","key2":"value2"}

# get:http://httpbin.org/get
# {"key":"value"}

# json:https://api.github.com/some/endpoint
# {'some':'data'}

# headers
# {'user-agent':'my-app/0.0.1'}







