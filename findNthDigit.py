class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 1
        while n > digit*9*10**(digit-1):
            n -= digit*9*10**(digit-1)
            digit += 1
        print(n)
        print(digit)
        a = n // digit
        print(n//digit)
        b = n % digit
        print(n%digit)
        if a == 0:
            c = 10 ** (digit-1) + a
        else:
            c = 10 ** (digit-1) + a -1
        print(10**(digit-1)+n//digit-1)
        if n%digit == 0:

            print(str(c )[digit-1])
            return int(str(c)[digit-1])
        else:
            print(str(c)[n%digit-1])
            return int((str(c+1)[b-1]))

Solution().findNthDigit(30)