#!/usr/bin/python3.4

classmates = ['Michael', 'Bob', 'Tracy']
print("%s" % classmates[0]);
print("%s" % classmates[1]);
print("%s" % classmates[2]);
# print("%s" % classmates[3]); error:IndexError
print("%s" % classmates[-1]); # 获取最后一个元素
print("%s" % classmates[-2]); # 获取倒数第二个元素

# list追加 append()
classmates.append('Adam');
print("%s" % classmates[-1]); # output:Adam
# 把元素插入到指定位置
classmates.insert(1, 'Jack');
print("%s" % classmates[0]); # Michael
print("%s" % classmates[1]); # Jack
print("%s" % classmates[2]); # Bob

# 要删除list末尾的元素，用pop()
classmates.pop();
print("%s" % classmates[-1]); # Tracy

# 删除指定位置 pop(i)
classmates.pop(0);
print("%s" % classmates[0]); # Jack

# 修改元素，直接赋值即可
classmates[0]='zzy';
print("%s" % classmates[0]); # zzy

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]

# list元素也可以是另一个list,取值的时候，相当于二维数组
s = ['python', 'java', ['asp', 'php'], 'scheme']
# 等价于
# p = ['asp', 'php']
# s = ['python', 'java', p, 'scheme']

print(s[0]);    # python
print(s[2][0]); # asp
print(s[2][1]); # php




