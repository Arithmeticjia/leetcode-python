def quick_sort(list, start, end):
    # 递归的退出条件
    if start >= end:
        return list
    # 设置起始元素为要寻找位置的基准元素
    mid = list[start]
    # left为序列左边的由左向右移动的游标
    left = start
    # right为序列右边的由右向左移动的游标
    right = end
    while left < right:
        # 从右边开始查找大于参考点的值
        # 则right向左移动
        while left < right and list[right] >= mid:
            right -= 1
        # 将right指向的元素放到left的位置上
        list[left] = list[right]
        # 从左边开始查找小于参考点的值
        # 则left向右移动
        while left < right and list[left] < mid:
            left += 1
        # 将left指向的元素放到right的位置上
        list[right] = list[left]

    # 退出循环后，left与right重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    list[left] = mid
    print(list)
    # 对基准元素左边的子序列进行快速排序
    quick_sort(list, start, left-1)
    # 对基准元素右边的子序列进行快速排序
    quick_sort(list, left+1, end)


if __name__ == '__main__':
    li = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    quick_sort(li, 0, len(li)-1)
    print(li)