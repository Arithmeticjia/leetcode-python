class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''nums = sorted(nums)
        print(nums)
        print(nums[len(nums)-k])
        return nums[len(nums)-k]'''
        count = len(nums)
        for i in range(0, count):
            for j in range(i + 1, count):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        print(nums)
        return nums[k-1]




if __name__ == '__main__':
    new  = Solution()
    new.findKthLargest([4,2,5,4,5,12,0,2,3,1,1,7,4],1)