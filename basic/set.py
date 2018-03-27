#!/usr/bin/python3.4
#coding=utf-8

# set 跟C++set一样 去重

s = set([1, 2, 2, 3])
print(s)  # 自动去重  {1, 2, 3}

# 添加元素 add(key)
s.add(4);
print(s)  #  {1, 2, 3, 4}
# 删除元素 remove(key)
s.remove(4);
print(s)  # {1, 2, 3}

# set的原理和dict一样，所以，同样不可以放入可变对象

# set 交集 set1 & set2

# set 并集 set | set2

