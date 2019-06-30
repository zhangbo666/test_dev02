__author__ = 'zhangbo'

from django.db import models

from module_app.models import Module

class TestCase(models.Model):

      '''

      用例表

      '''

      # 模块id
      module = models.ForeignKey(Module,on_delete=models.CASCADE)

      # 用例名称
      name = models.CharField("名称",max_length=50,null=False)

      # url地址
      url = models.TextField("URL",null=False)

      # 请求方法(1:GET 2:POST 3:PUT 4:DELETE )
      method = models.IntegerField("请求方法",null=False)

      # 请求头
      header = models.TextField("请求头",null=False)

      # 请求类型(1:form-data 2:json)
      parameter_type = models.IntegerField("参数类型",null=False)

      # 请求参数
      parameter_body = models.TextField("参数内容",null=False)

      # 返回结果
      result = models.TextField("返回结果",null=False)

      # 断言内容
      assert_text = models.TextField("断言内容",null=False)

      # 断言类型(1:包含contains 2:匹配mathches)
      assert_type = models.IntegerField("断言类型",null=False)

      # 创建时间
      create_time = models.DateTimeField(auto_now_add=True)



      def __str__(self):

            return self.name

