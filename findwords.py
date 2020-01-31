class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r = map(set, ['qwertyuiop','asdfghjkl','zxcvbnm'])
        first = 'qwertyuiop'
        second = 'asdfghjkl'
        third = 'zxcvbnm'
        ans = []
        for word in words:
            newword = word.lower()
            print(newword)
            print(len(newword))
            #for i in range(len(newword)):
            if all(newword[i] in first for i in range(len(newword))):
                ans.append(word)
            if all(newword[i] in second for i in range(len(newword))):
                ans.append(word)
            if all(newword[i] in third for i in range(len(newword))):
                ans.append(word)
        print(ans)
        return ans


if __name__ == '__main__':
    new = Solution()
    new.findWords(["Hello","Alaska","Dad","Peace"])