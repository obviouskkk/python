#!/usr/bin/python3.4
#coding=utf-8

# for ... in 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# range(i) 可以生成 0 --- i-1 的一个整数序列
lista=list(range(10))
print(lista)


# while循环，只要条件满足，就不断循环，条件不满足时退出循环
sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)
# break 跟C一样
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# continue 
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
