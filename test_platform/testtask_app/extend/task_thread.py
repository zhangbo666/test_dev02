#!/usr/bin/python3
#encoding:utf-8

__author__ = 'zhangbo'


import threading
import time
import json
import os
from testtask_app.models import TestTask
from testcase_app.models import TestCase
from test_platform import settings
from xml.dom.minidom import parse


BASE_PATH = settings.BASE_DIR.replace("\\","/")

EXTEND_DIR = BASE_PATH + "/testtask_app/extend/"

print ("EXTEND_DIR-->",EXTEND_DIR)


class TaskThread:

    def __init__(self,task_id):

        self.tid = task_id


    def run_cases(self):

        print ("运行某一个任务下面的所有测试用例")


        task = TestTask.objects.get(id=self.tid)

        # 1. 拿到任务对应用例的列表
        case_list = json.loads(task.cases)

        # 2. 修改任务状态为，执行中
        # task.status = 1
        # task.save()

        # 3. 拿到任务下面的所有的用例数据写到json文件
        test_data = {}

        for cid in case_list:

            case = TestCase.objects.get(id=cid)

            if case.method == 1:

                method = "get"

            elif case.method == 2:

                method = "post"

            if case.parameter_type == 1:

                parameter_type = "from"

            elif case.parameter_type == 2:

                parameter_type = "json"

            if case.assert_type == 1:

                assert_type = "contains"

            elif case.assert_type == 2:

                assert_type = "mathches"

            test_data[case.id] = {

                "url":case.url,
                "method":method,
                "header":case.header,
                "parameter_type":parameter_type,
                "parameter_body":case.parameter_body,
                "assert_type":assert_type,
                "assert_text":case.assert_text,

            }

        case_data = json.dumps(test_data)

        with(open(EXTEND_DIR + "test_data_list.json","w"))as f:

            f.write(case_data)

        # 4. 执行运行测试用例的文件，它会生成results.xml文件
        run_cmd = "python3 " + EXTEND_DIR + "run_task.py"

        os.system(run_cmd)

        time.sleep(2)

        # 4. 读取result.xml文件，把这里面的结果放到表里面

        # 5. 修改任务的状态，执行完成
        task = TestTask.objects.get(id=self.tid)

        task.status = 2

        task.save()

    def save_result(self ):

        # 打开xml文档
        dom = parse(EXTEND_DIR + 'results.html')

        # 得到文档元素对象
        root = dom.documentElement

        #获取（一组）标签
        testsuite = root.getElementsByTagName('testsuite')

        testsuite[0].getAttribute("errors")


    def run_tasks(self):

        print ("创建线程任务...")

        time.sleep(2)

        threads = []

        t1 = threading.Thread(target=self.run_cases)

        threads.append(t1)

        for t in threads:

            t.start()

        for t in threads:

            t.join()

    def run(self):

        threads = []

        t1 = threading.Thread(target=self.run_tasks)

        threads.append(t1)

        for t in threads:

            t.start()

        # for t in threads:

        #     t.join()


if __name__ == '__main__':

    print ("start")

    TaskThread(1).run()

    print ("end")



