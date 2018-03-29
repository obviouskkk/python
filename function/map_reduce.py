#!/usr/bin/python3.4
#coding=utf-8


# map 对每一个元素执行函数
# map (f, [x1, x2, x3, x4]) = [f(x1),f(x2),f(x3),f(x4)]
def sqr(x):
    return x * x;

r = map(sqr, range(1, 10));
print(list(r));  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# reduce 对前两个元素执行函数，结果和第三个元素一块执行 reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x, y):
    return x + y;
from functools import reduce
print(reduce(add, [1, 3, 5, 7, 9])); # 25
