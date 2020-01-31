class mysort():
    def bubble_sort(self,nums):
        # 冒泡排序
        count = len(nums)
        for i in range(0, count):
            for j in range(i + 1, count):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        print(nums)
        return nums


if __name__ == '__main__':
    new  = mysort()
    new.bubble_sort([4,2,5,4,5,12,0,2,3,1,1,7,4])