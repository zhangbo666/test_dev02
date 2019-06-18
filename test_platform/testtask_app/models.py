__author__ = 'zhangbo'

from django.db import models

class TestTask(models.Model):

      '''

      任务表

      '''


      # 任务名称
      name = models.CharField("名称",max_length=100,blank=False,default="")

      # 任务状态
      status = models.IntegerField("状态：",default=0)#未执行0、执行中1、执行成功2、执行失败3

      # 任务描述
      describe = models.TextField("描述",default="")

      # 关联用例
      cases = models.TextField("关联用例",default="")

      # 创建时间
      create_time = models.DateTimeField("创建时间",auto_now_add=True)

      def __str__(self):

            return self.name

