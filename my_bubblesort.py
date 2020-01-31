def bubble_sort_plus(nums):

    for i in range(len(nums) - 1):
        flag = False  # 改进后的冒泡，设置一个交换标志位
        for j in range(len(nums) - i - 1):

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        if not flag:
            return nums


def bubble_sort(nums):
    # n个数排序
    # 排序n-1次
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
        print('第{}趟结果{}'.format(i, nums))
    return nums


if __name__ == '__main__':
    # li = [4, 2, 5, 4, 5, 12, 0, 2, 3, 1, 1, 7, 4]
    li = [3, 4, 1, 2]
    print('最后结果{}'.format(bubble_sort(li)))
