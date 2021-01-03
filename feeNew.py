class Solution(object):
    def maxProfit(self, prices, fee):
        sum = 0
        for i in prices:
            sum = sum + i
        mean = sum / len(prices)

        b = [i * 0 for i in range(len(prices))]

        c = []
        inter = 0
        for i in range(len(prices)):
            if prices[i] > mean:
                b[i] = 0
            else:
                if prices[i] == mean:
                    b[i] = 2
                else:
                    b[i] = 1
        i = 0
        while i < 6:
            while i < 6 and b[i] >= 1:
                c.append(prices[i])
                i = i + 1
            if c != []:
                min_n = min(c)
                c.clear()
            while i < 6 and (b[i] == 0 or b[i] == 2):
                c.append(prices[i])
                i = i + 1
            if c != []:
                max_n = max(c)
                c.clear()
            inter = inter + (max_n - min_n) - fee
        return inter


if __name__ == "__main__":
    print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2))