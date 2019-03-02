from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def say_hello(request):

    name = request.GET.get("name","")

    talk = []

    for n in  range(3):

        # print ("hello," + name)

        talk.append("hello," + name + '\n')

    return HttpResponse(talk)
