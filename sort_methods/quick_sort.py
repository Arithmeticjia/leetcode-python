def quickSort(data, start, end):
    i = start
    j = end
    # i与j重合时，一次排序结束
    if i >= j:
        return
    # 设置最左边的数为基准值
    flag = data[start]
    while i < j:
        while i<j and data[j] >= flag:
            j -= 1
        # 找到右边第一个小于基准的数，赋值给左边i。此时左边i被记录在flag中
        data[i] = data[j]
        while i<j and data[i] <= flag:
            i += 1
        # 找到左边第一个大于基准的数，赋值给右边的j。右边的j的值和上面左边的i的值相同
        data[j] = data[i]
    # 由于循环以i结尾，循环完毕后把flag值放到i所在位置。
    data[i] = flag
    # 除去i之外两段递归
    quickSort(data, start, i-1)
    quickSort(data, i+1, end)

# quickSort(data,0, len(data)-1)
# print(data)
