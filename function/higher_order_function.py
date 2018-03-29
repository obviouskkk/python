#!/usr/bin/python3.4
#coding=utf-8

# 变量可以指向函数 本质应该是函数指针的赋值
def A():
    print("hello world");

p = A;
A()
p()

# 把函数当参数传入
def add(x, y, f):
    return f(x) + f(y)


print(add(-1, -5 , abs)) # 6
