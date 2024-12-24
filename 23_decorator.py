# def birni_qosh(num):
#     return num + 2
#
#
# func = birni_qosh
# birni_qosh(12)
# func(12)
# del birni_qosh
# print(func(2))
# birni_qosh(21)
import logging
import math
import time

# def tashqi_func():
#     print("tashqi func ishladi")
#
#     def ichki():
#         print("ichkki funksiya ishladi")
#
#     ichki()
#
#
# tashqi_func()
# from typing import Callable
#
#
# def uppercase_decorate(func: Callable) -> Callable:
#     def inner(message: str) -> str:
#         result = func(message)  # salom dunyo
#         return result.upper()
#
#     return inner
#
#
# # a = uppercase_decorate(salom_ber)
# # print(a("dunyo"))
# @uppercase_decorate
# def salom_ber(message: str) -> str:
#     return f"salom {message}"
#
# print(salom_ber("dunyo"))
#
# def timer_decorater(func):
#     def inner(messege):
#         begin = time.time()
#         r = func(messege)
#         end = time.time()
#         print(f"{func.__name__} funksiyasi {end - begin} ishladi")
#         return r
#
#     return inner
#
#
# @timer_decorater
# def salom_ber(m):
#     time.sleep(1)
#     return f"salom {m}"


# begin = time.time()
# print(salom_ber("dunyo"))
# end = time.time()
# print(f"salom ber funksiyasi {end - begin} ishladi")

# @timer_decorater
# def factorilas(num):
#     time.sleep(1)
#     return math.factorial(num)
#
#
# print(factorilas(200))


# def decor1(func):
#     def inner():
#         print(func.__name__)
#         x = func()
#         return x ** 2
#
#     return inner
#
#
# def decor2(func):
#     def inner():
#         x = func()
#         print(func.__name__)
#         return x * 2
#
#     return inner
#
#
# @decor1
# @decor2
# def num():
#     return 10
#
#
# print(num())
from typing import Callable


def split(sep="") -> Callable:
    def decorator(func: Callable):
        def inner(message: str) -> str:
            result = func(message)  # salom dunyo
            print(result)
            return result.split(sep=sep)

        return inner

    return decorator


def uppercase_decorate(func: Callable) -> Callable:
    def inner(message: str) -> str:
        result = func(message)  # salom dunyo
        return result.upper()

    return inner


import logging

logging.basicConfig(
    filename="log.log",
    level=logging.DEBUG,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)


class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        logging.info("logger decoratorio ishladi")
        a = self.func(*args, **kwargs)
        logging.info("logger decoratorio tugadi")
        return a


@Logger
@split(sep=",")
@uppercase_decorate
def salom_ber(message: str) -> str:
    return f"salom {message}"


print(salom_ber("dunyo"))

# @Logger
# def salom_ber(*args, **kwargs):
#     for i in args:
#         print(f"salom {i}")
#
#     for k, v in kwargs.items():
#         print(f"salom {k} {v}")
#
#     return "tugadi"
#
#
# salom_ber("ali", "vali", alisher="Aliyev")
