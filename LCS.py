class Solution:
    def LCS(self, s1, s2):
        lcs = 0
        res = ''
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        for i in range(len(s1)):
            if s1[i - lcs: i + 1] in s2:
                res = s1[i - lcs: i + 1]
                lcs += 1

        if not res:
            return '-1'
        else:
            return res


if __name__ == '__main__':
    print(Solution().LCS("1AB2345CD", "12345EF"))
