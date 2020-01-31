# res = ['']
# m = ['a', 'b', 'c']
# n = ['d', 'e', 'f']
# tem = []
# for x in res:
#     for y in m:
#         for k in n:
#             tmp = x + y + k
#             tem.append(res)
#     print(tem)

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
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                nums.pop(i)
                # print(len(nums))
        # print(nums)
        return len(nums)


if __name__ == '__main__':
    Solution().removeElement([0,4,4,0,4,4,4,0,2],4)