# 作业题
# 题目1 使用进程  打印1到5   跟打印6-10

# 题目2 使用线程  一个打印10次hello  一个打印10次world

"""
import multiprocessing
from time import sleep


def func(data):
    for i in data:
        sleep(0.2)
        print(multiprocessing.current_process().name,i)

def func2(data):
    for i in data:
        sleep(0.2)
        print(multiprocessing.current_process().name,i)

if __name__ == '__main__':
    multiprocessing.Process(target=func, args=(range(1, 6),)).start()
    multiprocessing.Process(target=func2, args=(range(6, 11),)).start()
"""
import threading


def func(data):
    for i in range(10):
        print("hello")
def func2(data):
    for i in range(10):
        print("world")


    threading.Thread(target=func).start()

    threading.Thread(target=func2).start()
