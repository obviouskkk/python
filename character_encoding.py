#!/usr/bin/python3.4

# Python的字符串类型是str，在内存中以Unicode表示
# 把中文转成整数 ord
a = ord('中');
print(a);
# 把整数转成对应的中文 chr
print(chr(20013));

# 网络传输用的是bytes, 可以转换
# Python对bytes类型的数据用带b前缀的单引号或双引号表示  eg: b'ABC'
# Unicode表示的str通过encode()方法可以编码为指定的bytes

print( 'ABC'.encode('ascii'));
print('中文'.encode('utf-8')); # b'\xe4\xb8\xad\xe6\x96\x87'

# 从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print( b'ABC'.decode('ascii'));
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'));

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print("b'ABC'的len():", len(b'ABC'));

# 格式化输出，和C语言一样，但是中间不使用 逗号，而是使用 % 分开
zzy= 'helloworld';
print("zzy = %s" % zzy);
inta = 12;
print("inta = %d" % inta);

