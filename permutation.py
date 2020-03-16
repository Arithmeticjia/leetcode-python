class Solution:

    def permutation(self, s):
        res = []
        if len(s) == 1:
            return list(s)
        for i, x in enumerate(s):
            n = s[:i] + s[i+1:]
            for y in self.permutation(n):
                res.append(x+y)
        return list(set(res))


if __name__ == '__main__':
    print(Solution().permutation('abc'))