class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result = []
        fix = dict()
        for word in words:
            for i in range(len(pattern)):
                fix[pattern[i]] = word[i]
            #print(fix)
            func = lambda z: dict([(x, y) for y, x in z.items()])
            #print(func(fix))
            #print(func(func(fix)))
            fix = func(func(fix))
            if all(word[i] == fix.get(pattern[i]) for i in range(len(fix))):
                result.append(word)
                fix = {}
        print(result)
        return result


Solution().findAndReplacePattern(["badc","abab","dddd","dede","yyxx"],"baba")