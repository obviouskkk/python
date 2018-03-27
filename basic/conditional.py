#!/usr/bin/python3.4
#coding=utf-8

age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
else: # :必须
    print('your age is', age)
    print('teenager')  # 缩进 也会打印

    print('teenager')  # 这个空一行 也会打印
print('teenager')  # 这个不缩进不进入判断了 也会打印
# str不能直接和整数比较，必须先把str转换成整数。int()
