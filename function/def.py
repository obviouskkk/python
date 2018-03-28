#!/usr/bin/python3.4
#coding=utf-8

def my_max(x, y):
    if not isinstance(x, (int , float)) or not isinstance(y, (int, float)):
        raise TypeError('Error Type');
    if x == 0:
        pass
    if x > y :
        print("x is big")
        return x
    else:
        return y

x = 'str'
y = 20
# print(my_max(x, y))

# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。

# 类型检查函数 isinstance()
def my_abs(x):
    if not isinstance(x, (int, float)):         # x z只能是int 或者 float
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print (my_abs(-1));
# print (my_abs('a')); # raise error

# 默认参数
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def power(x, n=2):  # 一是必选参数在前，默认参数在后
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

x = 2
n = 3
print("%d的%d次方是:%d " % (x , n , power(x, n)))


# 不按顺序提供默认参数，要显式赋值
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Adam', 'M', city='Tianjin');
enroll('Bob', 'M', 7)


# 可变参数 *numers
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
# *nums表示把nums这个list的所有元素作为可变参数传进去
def iterator(*numers):
    for i in numers:
        print(i);

iterator(1, 2 ,3 , 4);

# <<<<<<<<<<<关键字参数 **kw
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# 简单写法
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('zzy', 30, **extra) # kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

# <<<<<<<命名关键字参数
# 限制关键字参数的名字，就可以用命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)

# extra = {'city':'shanghai', 'job':'manong', 'gf':'zt'}  # person() got an unexpected keyword argument 'gf'
extra = {'city':'shanghai', 'job':'manong'}
person('zzy', 22, **extra); 

# <<<<<<< 参数组合
# 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
    

# <<<< 递归函数

def fact(n):  # 阶乘
    if n==1:
        return 1
    return n * fact(n - 1)

n = 12;
print('%d的阶乘是%d' %(n, fact(n)))












