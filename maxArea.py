class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                res = max(res,(right-left)*height[left])
                left += 1
            else:
                res = max(res,(right-left)*height[right])
                right -= 1
        return res

if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))