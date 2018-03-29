#!/usr/bin/python3.4
#coding=utf-8

# generator函数的“调用”实际返回一个generator对象

def grep(pattern):
    print("Searching for", pattern)
    while True:
        print("wait yield")
        line = (yield)
        if pattern in line:
            print(line)
        else:
            print("Not metch")

search = grep('coroutine')
next(search)
#output: Searching for coroutine
#search.send("I love you")
#search.send("Don't you love me?")
search.send("I love coroutine instead!")
#output: I love coroutine instead!
#search.close()

print("hello")
