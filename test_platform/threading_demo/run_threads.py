__author__ = 'zhangbo'


import threading

def task1():

    print ("任务1")


def task2():

    print ("任务2")



if __name__ == '__main__':


    task1()
    task2()