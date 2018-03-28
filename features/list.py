#!/usr/bin/python3.4
#coding=utf-8

# list(range(x, y))  生成整型
print(list(range(1, 11)))

# 
print([x * x for x in range(1, 11)]) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([ x* 2 + 1 for x in range(1 , 11)]); # [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

# 加上if筛选
print([x * x for x in range(1, 11) if x % 2 == 0])  #  [4, 16, 36, 64, 100]

# 两次循环生成全排
print([m + n for m in 'ABC' for n in 'XYZ'])  # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

import os
print([d for d in os.listdir('.')])


