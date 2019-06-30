__author__ = 'zhangbo'

import sys
import json
import unittest
import requests
from ddt import ddt,data,file_data,unpack
from os.path import dirname,abspath

BASE_DIR = dirname(dirname(dirname(abspath(__file__))))
print ("运行测试文件：",BASE_DIR)

BASE_PATH = BASE_DIR.replace("\\","/")
print ("运行测试文件：",BASE_PATH)

sys.path.append(BASE_PATH)

TASK_PATH = BASE_PATH + "/testtask_app/extend/"
print ("运行测试文件：",TASK_PATH)

@ddt
class InterfaceTest(unittest.TestCase):

    @unpack
    @file_data("test_data_list.json")
    def test_run_casess(self,url,method,header,parameter_type,parameter_body,assert_type,assert_text):

        if header == "{}":

            header_dict = {}

        else:

            header_dict = header.replace("\'","\"")

        if parameter_body == "{}":

            parameter_dict = parameter_body

        else:

            parameter_str = parameter_body.replace("\'","\"")
            parameter_dict = json.loads(parameter_str)

        if method == "get":

            if parameter_type == "from":

                r = requests.get(url,headers=header_dict,params=parameter_dict)

                # self.assertIn(assert_text,r.text)

        if method == "post":

            if parameter_type == "from":

                r = requests.post(url,headers=header_dict,data=parameter_dict)

                print (r.text)

                # self.assertIn(assert_text,r.text)

            elif parameter_type == "json":

                r = requests.post(url,headers=header_dict,json=parameter_dict)

                # self.assertIn(assert_text,r.text)


if __name__ == '__main__':

    unittest.main()

