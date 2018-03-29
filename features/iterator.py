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

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 一类是集合数据类型，如list、tuple、dict、set、str等
# 一类是generator，包括生成器和带yield的generator function。
# 可以使用isinstance()判断一个对象是否是Iterator对象：
print(isinstance('abc', Iterator)); # False 可迭代，但不是迭代器
print(isinstance({}, Iterator));    # False 可迭代，但不是迭代器
print(isinstance([], Iterator));    # Fales 可迭代，但不是迭代器

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。


# 总结
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。














