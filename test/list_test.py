# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2018/12/6 10:06'
import time
import random
import string
def test1():
    list1 = []
    start = time.perf_counter()
    for i in range(10000000):
        # print(i)
        # ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        list1.append(i)
        # print(len(list1))
        if i %1 ==0:
            print(i)
        # i+=1
    end = time.perf_counter()
    print(end-start)

    # print(time.perf_counter())
    # print(time.perf_counter())
    # print(time.process_time())

def test2():
    start = time.perf_counter()
    list1 = []
    for i in range(10000000):
        print(i)
        i+=1
    end = time.perf_counter()
    print(end-start)
    # print(time.process_time())

def test3():
    dict1 = {}
    dict1.setdefault()

test1()