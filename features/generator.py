#!/usr/bin/python3.4
#coding=utf-8

# 生成器
# 在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间

g = (x * x for x in range(10)) # 把列表生成式的[]换成()
# m每次调用 next(g) 可以获得下一个元素
for n in g:
    print(n);

# 菲波那切数列
def fib(x):
    n ,a ,b = 1, 0, 1;
    if x == 1:
        print(a);
    while n < x:
        print(b);
        a , b = b, a + b; # 相当于 t = (b, a + b) # t是一个tuple
        n = n + 1;
    return None;

fib(5)

# 生成器版本的  如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
print("生成器版本的");
def fib(x):
    n ,a ,b = 1, 0, 1;
    while n < x:
        yield b;
        a , b = b, a + b; # 相当于 t = (b, a + b) # t是一个tuple
        n = n + 1;
    return None;

for n in fib(6):
    print(n);

# 例子
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

x = odd()

print(next(x));
print(next(x));
print(next(x));



