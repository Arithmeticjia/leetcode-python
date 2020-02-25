class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        nums = sorted(nums)
        sum = 0
        for i in range(0, len(nums) - 1, 2):
            sum += nums[i]
        return sum


if __name__ == '__main__':
    print(Solution().arrayPairSum([1, 4, 2, 3]))
