from django.shortcuts import render

# Create your views here.



# 用例管理
def testcase_manage(request):

    return render(request,"testcase.html",{"type":"debug"})