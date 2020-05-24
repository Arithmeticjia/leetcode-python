# -*- coding:UTF-8 -*-
import sys

list = [1, 2, 3, 4]

it = iter(list)

# 常规for语句进行遍历
# for i in it:
#     print(i, end="")

# next()函数
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()