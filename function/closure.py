#!/usr/bin/python3.4
#coding=utf-8

# 函数里面定义函数 , 函数里面还可以返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中
f = lazy_sum(1, 3, 5, 7, 9)
print(f()) # 25

# 调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f);  # False 不相同

# 注意 ：返回的函数并没有立刻执行，而是直到调用了f()才执行

