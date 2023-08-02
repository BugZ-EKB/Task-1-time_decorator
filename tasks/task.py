from typing import Dict
import time
from time import sleep

execution_time: Dict[str, float] = {}

def time_decorator(fn):
    def wrapper(a, b, d):
        start = time.time()
        fn(a,b,d)
        end = time.time()
        c = end-start + d
        execution_time[str(fn.__name__)] = c
    return wrapper
    pass
# @time_decorator
# def func_add(a: int, b: int):
#     sleep(0.2)
#     return a + b
#
# func_add(10, 20)
# print(execution_time)
# print(execution_time['func_add'])
# 0.212341254