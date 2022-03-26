#!/usr/bin/python3
# -*- encoding:utf-8 -*-
# author: king
# file: process_demo.py
# datetime: 2022/03/25 23:03:55

from multiprocessing import Process, Pool
import os, time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def work_job(n):
    print(f"当前进程: {os.getpid(), os.getppid()}, 开始")
    time.sleep(n)
    print(f"当前进程: {os.getpid()}, 结束")
    return n


def main0():
    p = []
    for i in range(5):
        p1 = Process(target=work_job, args=(i, ))
        p.append(p1)

    for s in p:
        s.start()

    for s in p:
        s.join()


def main1():
    p = Pool(5)
    p.map_async(work_job, range(5))
    p.close()
    p.join()


def main2():

    def fun_01(args):
        print(f"end_time: {args}, {time.ctime()}")

    p = Pool(5)
    for i in range(5):
        p.apply_async(work_job, args=(i, ), callback=fun_01)
    p.close()
    p.join()
    print("done")


def main():
    with ProcessPoolExecutor(max_workers=5) as ex:
        ex.map(work_job, range(5))


if __name__ == '__main__':
    main()