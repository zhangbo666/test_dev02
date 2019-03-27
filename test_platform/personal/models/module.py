__author__ = 'zhangbo'

from django.db import models

from personal.models.project import Project

# Create your models here.


class Module(models.Model):

      '''

      模块表

      '''

      project = models.ForeignKey(Project,on_delete=models.CASCADE)

      name = models.CharField(max_length=50,null=False)

      describe = models.TextField(default="",max_length=50)

      create_time = models.DateTimeField(auto_now_add=True)



      # def __str__(self):
      #
      #       return self.name