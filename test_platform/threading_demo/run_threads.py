#!/usr/bin/python3
#encoding:utf-8

__author__ = 'zhangbo'


import threading
import time


def task1():

    time.sleep(1)

    print ("task_1")


def task2():

    # time.sleep(2)

    print ("task_2")

def run_talk1():

    threads = []

    t1 = threading.Thread(target=task1)

    threads.append(t1)

    t2 = threading.Thread(target=task2)

    threads.append(t2)

    for t in threads:

        t.start()

    # for t in threads:
    
    #     t.join()

def run_talk2():

    threads = []

    t1 = threading.Thread(target=run_talk1)

    threads.append(t1)

    for t in threads:

        t.start()

    # for t in threads:
    
    #     t.join()

if __name__ == '__main__':

    print ("start")

    run_talk2()

    print ("parse")

    run_talk1()

    print ("end")




    