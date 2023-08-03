from typing import Dict
import time
from time import sleep

execution_time: Dict[str, float] = {}

def time_decorator(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        c = end-start
        execution_time[str(fn.__name__)] = c
        return fn(*args, **kwargs)
    return wrapper
    pass
# @time_decorator
# def func_add(a: int, b: int, sleep_time: int):
#     sleep(sleep_time)
#     return a + b
#
# print(func_add(10, 20, 0.1))
# print(execution_time)
# print(execution_time['func_add'])
# 0.212341254