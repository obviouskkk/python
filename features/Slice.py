#!/usr/bin/python3.4
#coding=utf-8

# list 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[1:3]); # 取 x - y 个元素 包括 x 不包括y  第一个和第二个
print(L[:3]); # 前三个
print(L[-3:]); # 后三个
print(L[-3:-1]); # 倒数第二和倒数第一个

# tuple切片
t = ('Michael', 'Sarah', 'Tracy', 'Bob', 'Jack');
print(t[1:3]); # 取 x - y 个元素 包括 x 不包括y  第一个和第二个
print(t[:3]); # 前三个
print(t[-3:]); # 后三个
print(t[-3:-1]); # 倒数第二和倒数第一个

# 字符串切片
string='hello world'
print(string[1:3]); # 取 x - y 个元素 包括 x 不包括y  第一个和第二个
print(string[:3]); # 前三个
print(string[-3:]); # 后三个
print(string[-3:-1]); # 倒数第二和倒数第一个




