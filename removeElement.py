class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # k = 0
        # for i in nums:
        #     if i != val:
        #         nums[k] = i
        #         k += 1
        # return k
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)


if __name__ == '__main__':
    Solution().removeElement([0, 4, 4, 0, 4, 4, 4, 0, 2], 4)
