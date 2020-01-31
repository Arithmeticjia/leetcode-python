def execute_time(func):
    from time import time

    # 定义嵌套函数，用来打印出装饰的函数的执行时间
    def wrapper(*args, **kwargs):
        # 定义开始时间
        start = time()
        # 执行函数
        func_return = func(*args, **kwargs)
        # 定义结束时间
        end = time()
        # 打印方法名称和其执行时间
        print('{}() execute time: {}s'.format(func.__name__, end-start))
        # 返回func的返回值
        return func_return

    # 返回嵌套的函数
    return wrapper


@execute_time
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        # for i, num in enumerate(nums):
        #     hashmap[num] = i
        # for j, num in enumerate(nums):
        #     k = hashmap.get(target-num)
        #     if k is not None and j != k:
        #         return [j, k]
        for i, n in enumerate(nums):
            if target - n in hashmap:
                return [hashmap.get(target - n), i]
            hashmap[n] = i


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
