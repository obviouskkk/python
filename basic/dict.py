#!/usr/bin/python3.4
#coding=utf-8

# dict 字典 类似unodermap

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob']); # 75 注意：不能省略‘’

# 添加
d['Adam'] = 67
print(d['Adam']) # 67

# 如果key不存在，并且不是添加语句，dict就会报错

# 判断key是否存在
print( 'Thomas' in d) # False
# 或者通过get() , get()可以设置默认返回值
print(d.get('Thomas')) # None
print(d.get('Thomas', -1)) # -1

# 删除key pop(key)
d.pop('Bob');

# list 不能作为key



