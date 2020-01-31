class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a

        b = b.zfill(len(a))
        a = a[::-1]
        b = b[::-1]
        res = ''
        count = 0
        for i, num in enumerate(a):
            b_sum = int(b[i])
            res = res + str((int(num) + b_sum + count) % 2)  # 二进制加法运算
            if int(num) + b_sum + count > 1:  # 是否进位
                count = 1
            else:
                count = 0
        if count == 1:  # 最高位
            res = res + "1"

        print(res[::-1])
        return res[::-1]


if __name__ == '__main__':
    test = Solution()
    test.addBinary('111', '1')