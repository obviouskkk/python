#!/usr/bin/python3.4

# tuple一旦初始化就不能修改
# 没有append()，insert()这样的方法。
# 其他获取元素的方法和list是一样的
classmates = ('Michael', 'Bob', 'Tracy')

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
classmate = (1, )
print(classmate); # (1,)


# uple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
# tuple如果包含了 list。可以对list修改，变相修改tuple
t = ('a', 'b', ['A', 'B']);
print(t);
t[2][0] = 'X';
t[2][1] = 'Y';
print(t);


