#!/usr/bin/python3
#encoding:utf-8

__author__ = 'zhangbo'


import threading
import time


def task1():

    print ("task_1")
    time.sleep(2)


def task2():

    print ("tasl_2")
    time.sleep(3)


def run_talk():

    threads = []

    t1 = threading.Thread(target=task1())

    threads.append(t1)

    t2 = threading.Thread(target=task2())

    threads.append(t2)

    for t in threads:

        t.run()

    for t in threads:

        t.join()

if __name__ == '__main__':

    run_talk()
    print ("finish end")