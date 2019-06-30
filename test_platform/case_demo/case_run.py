# !/usr/bin/python

__author__ = 'zhangbo'

import unittest
import requests
import sys
from ddt import ddt,data,file_data,unpack
import json


#ddt参数化
@ddt
class FooTestCase(unittest.TestCase):

    @data(3,4,12,33)
    def test_larger_than_one(self,value):

        print ("参数--->",value)


    @data([3,2],[4,3],[5,3])
    @unpack
    def test_larget_than_two(self,first,second):

        print ("第一个数",first)
        print ("第二个数",second)


    @data(["get","https://api.github.com/events","{}","github"],
          ["post","http://httpbin.org/post","{'key':'value'}","61.149.103.121"])
    @unpack
    def test_list_extracted_info_arguments1(self,method,url,par,assert_text):

        print ("test_list_extracted_info_arguments1:")
        # print ("请求方法",method)
        # print ("请求地址",url)
        # print ("请求参数",par)
        # print ("断言的结果",assert_text)

        json_par = par.replace("\'","\"")
        # print (json_par)
        # print (type(json_par))

        try:

            payload = json.loads(json_par)
            # print (type(payload))

        except json.decoder.JSONDecodeError:

            print ("参数类型错误")

        if method == "post":

            r = requests.post(url,data=payload)
            result1 = r.text
            print ("结果-->post",result1)
            print (type(result1))
            print ("\n")

            self.assertIn(assert_text,result1)

        if method == "get":

            r = requests.get(url,params=payload)
            result2 = r.text
            print ("结果-->get",result2)
            print (type(result2))

            print ("\n")

            self.assertIn(assert_text,result2)


    @file_data("test_data_list.json")
    def test_list_extracted_info_arguments2(self,method,url,par,assert_text):

        print ("test_list_extracted_info_arguments2:")

        # print ("请求方法",method)
        # print ("请求地址",url)
        # print ("请求参数",par)
        # print ("断言的结果",assert_text)

        json_par = par.replace("\'","\"")
        # print (json_par)
        # print (type(json_par))
        try:

            payload = json.loads(json_par)
            # print (type(payload))

        except json.decoder.JSONDecodeError:

            print ("参数类型错误")

        if method == "post":

            r = requests.post(url,data=payload)
            result1 = r.text
            # print ("结果",result1)
            print ("\n")

            self.assertIn(assert_text,result1)

        if method == "get":

            r = requests.get(url,params=payload)
            result2 = r.text
            # print ("结果",result2)
            print ("\n")

            self.assertIn(assert_text,result2)


#unittest执行
# class MyTest(unittest.TestCase):
#
#     def test_case1(self):
#
#         r = requests.get('https://api.github.com/events')
#         result = r.text
#         print (type(result))
#         print(result)
#         print (result[0]["id"])
#         self.assertIn("github",result)
#         self.assertEqual(2+2,4)
#
#     def test_case2(self):
#
#         r = requests.post('http://httpbin.org/post',data = {'key':'value'})
#         result = r.text
#         print (type(result))
#         print (result)
#         self.assertIn("61.149.103.121",result)
#
#     def test_case3(self):
#
#         r = requests.post('http://httpbin.org/post',data = {'key':'value'})
#         result = r.json()
#         print (type(result))
#         print (result)
#         self.assertIn("61.149.103.121, 61.149.103.121",result["origin"])
#
#     def test_case4(self):
#
#         self.assertEqual(2+2,4)



if __name__ == '__main__':

    unittest.main(verbosity=2)

# print ("\U0001f6a8")

# print (sys.getdefaultencoding())

# print (sys.stdout.encoding)
