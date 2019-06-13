__author__ = 'zhangbo'

from django.db import models

class Testtask(models.Model):

      '''

      任务表

      '''


      # 任务名称
      name = models.CharField("任务名称",max_length=50,null=False)

      # 任务状态
      status = models.IntegerField("任务状态",default=0)

      # 任务描述
      describe = models.TextField("任务描述",null=False)

      # 创建时间
      create_time = models.DateTimeField(auto_now_add=True)

      def __str__(self):

            return self.name

