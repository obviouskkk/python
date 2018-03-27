#!/usr/bin/python3.4
#coding: utf-8

# 整型
print(123);
print(-1);
# 浮点数
print(1.23e9); # 1.23x10^9
print(1.2e-5); # 0.000012
# 字符串
print('I\'m ok.'); # \可以转义
# 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
print('\\\t\\');
print(r'\\\t\\');
#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''line1
        line2
        line3''');
# 布尔值
# and == && or == || not == ！
print(1 > 2  or 2 > 1);
print(1 < 2 and 2 < 3);
print(not 1 > 2);

# 空值 None != 0

# 变量
a = 100
print("a = ", a);
a = 'hello world';
print("a = ", a);

# 除法 保留小数
print("19/3 = ", 19/3);
# 除法取整
print("9//4 = ", 9//4);
# 除法求模
print("9%4 = ", 9%4);
# 常量 ,不存在常量
PI = 3.14159265359
