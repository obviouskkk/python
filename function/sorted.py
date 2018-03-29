#!/usr/bin/python3.4
#coding=utf-8

# 对绝对值排序
print(sorted([36, 5, -12, 9, -21], key=abs))

# 不区分大小写排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))


