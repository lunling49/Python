#!/usr/bin/python
# -*- coding: UTF-8 -*-
import string
import random

# random函数
print(random.randint(1, 50))            # 产生 1 到 50 的一个整数型随机数
print(random.randrange(0, 101, 2))      # 随机选取 0 到 100 间的偶数
print(random.random())                  # 产生 0 到 1 之间的随机浮点数
print(random.uniform(1, 10))            # 产生  1 到 10 之间的随机浮点数，区间可以不是整数
print(random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()'))    # 从序列中随机选取一个元素
print(random.sample('zyxwvutsrqponmlkjihgfedcba', 5))           # 多个字符中生成指定数量的随机字符

# 从a-zA-Z0-9生成指定数量的随机字符：
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print(ran_str)

# 多个字符中选取指定数量的字符组成新字符串：
print(''.join(random.sample(['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i'], 5)))

# 随机选取字符串：
print(random.choice(['剪刀', '石头', '布']))

# 打乱排序
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(a)
print(a)
