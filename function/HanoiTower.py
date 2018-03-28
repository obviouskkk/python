#!/usr/bin/python3.4
#coding=utf-8


# 练习：汉诺塔
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b );  # 把a上的前n-1个盘子移动到b
        move(1, a, b, c);       # 把a上的最后一个盘子移到c
        move(n-1 ,b , a, c);    # 把b上的n-1个盘子移到c


n=int(input('请输入汉诺塔的层数：'))
move(n,'A','B','C')
