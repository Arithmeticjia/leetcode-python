"""
58. 最后一个单词的长度
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[i] == ' ':
                return n - 1 - i
        return n


if __name__ == '__main__':
    Solution().lengthOfLastWord(" ")