class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return []
        total_l = []
        total_l.append([None])          # 0组括号时记为None
        total_l.append(["()"])          # 1组括号只有一种情况
        for i in range(2, n+1):         # 开始计算i组括号时的括号组合
            l = []
            for j in range(i):                  # 开始遍历 p q ，其中p+q=i-1 , j 作为索引
                now_list1 = total_l[j]          # p = j 时的括号组合情况
                now_list2 = total_l[i-1-j]      # q = (i-1) - j 时的括号组合情况
                for k1 in now_list1:
                    for k2 in now_list2:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2 = ""
                        el = "(" + k1 + ")" + k2
                        l.append(el)    # 把所有可能的情况添加到 l 中
            total_l.append(l)    # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
        print(total_l)
        return total_l[n]


    def generateParenthesis_n(self, n: int):
        dp = [[] for _ in range(n + 1)]     # dp[i]存放i组括号的所有有效组合
        print(dp)
        dp[0] = ['']  # 初始化dp[0]
        for i in range(1, n + 1):           # 遍历dp[i],计算dp[i]
            for p in range(i):              # 遍历p，括号？
                l1 = dp[p]                  # 得到dp[p]的所有有效组合
                print('l1', l1)
                l2 = dp[i - 1 - p]          # 得到dp[q]的所有有效组合
                for k1 in l1:
                    for k2 in l2:
                        print("({0}){1}".format(k1, k2))
                        dp[i].append("({0}){1}".format(k1, k2))
                        print(dp)
        return dp[n]


    def generateParenthesis_j(self, n: int):
        res = [[] for _ in range(n+1)]
        print(res)
        res[0] = ['']
        for i in range(1, n+1):
            for j in range(i):
                p = res[j]
                q = res[i-j-1]
                for k1 in p:
                    for k2 in q:
                        res[i].append('(' + k1 +')' + k2)
        return res[n]


if __name__ == '__main__':
    test = Solution()
    print(test.generateParenthesis_j(2))