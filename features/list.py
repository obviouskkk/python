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

# 使用多个变量
dicA = {"zzy":23, "aut":25, "eden":30}
for k, v in dicA.items():
    print(k, " = ", v);

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)];
print(L2)

# test
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

