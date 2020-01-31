class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_exist = sum(nums)
        all_full = sum([i for i in range(len(nums)+1)])
        return all_full - all_exist


if __name__ =='__main__':
    test = Solution()
    print(test.missingNumber([3,1,0]))