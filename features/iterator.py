#!/usr/bin/python3.4
#coding=utf-8

# list迭代
L = [1,2 ,3 ,4 , 5, 6]
for i in L:
    print(i);

# 字符串迭代
x = 'zzy'
for i in x:
    print(i);

# 字典迭代
dic = {'zzy':'shuai', 'aut':'chou'}
for i in dic:
    print(i); # aut zzy 只迭代key 前后顺序不一定

# 迭代value
for i in dic.values():
    print(i); # chou shuai 前后顺序不一定

# 同时迭代key和value
for i in dic.items():
    print(i); # ('zzy', 'shuai') ('aut', 'chou')

# 判断一个对象是否可迭代
from collections import Iterable
print(isinstance('abc', Iterable));  # True
print(isinstance([1,2 ,3], Iterable)); # True
print(isinstance(123, Iterable)); # False

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value);
