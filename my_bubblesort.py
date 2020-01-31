def bubble_sort_plus(nums):

    for i in range(len(nums) - 1):
        flag = False  # 改进后的冒泡，设置一个交换标志位
        for j in range(len(nums) - i - 1):

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        if not flag:
            return nums  # 这里代表计算机偷懒成功 (〃'▽'〃)


def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == '__main__':
    li = [4, 2, 5, 4, 5, 12, 0, 2, 3, 1, 1, 7, 4]
    print(bubble_sort(li))