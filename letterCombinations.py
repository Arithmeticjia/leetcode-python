# 递归
class Solution:
    def letterCombinations(self,digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_str = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(num_str[int(digits)])
        res = []
        res_suffix = Solution().letterCombinations(digits[1:])
        print(res_suffix)
        for x in num_str[int(digits[0])]:
            res.extend([x+y for y in res_suffix])
        print(res)
        return res


class Solution_2:
    def letterCombinations(self,digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_str = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        result = list()
        if not digits:
            return result
        chars = [num_str.get(d) for d in digits]
        tmp = [[]]
        for pool in chars:
            tmp = [x + [y] for x in tmp for y in pool]

        for prod in tmp:
            result.append(''.join(prod))

        return result


class Solution_3:
    def letterCombinations(self, digits):
        m = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
            }
        if not digits:
            return []
        res = ['']
        for i in digits:
            res = [x + y for x in res for y in m[i]]
            print(m[i])
            # print(res)
        return res


if __name__ == '__main__':
    test = Solution_3()
    test.letterCombinations('234')