class Solution(object):
    # 将一个数从2除到N - 1
    # 遇到能整除的就不是素数，反之就是
    def minSteps(self, n):
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                print(d)
                n /= d
            d += 1
        return ans


if __name__ == '__main__':
    print(Solution().minSteps(20))
