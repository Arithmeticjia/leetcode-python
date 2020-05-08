class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        allCity = set()
        beginCity = set()
        for path in paths:
            allCity.add(path[0])
            allCity.add(path[1])
            beginCity.add(path[0])
        # set.pop()随机移除一个元素，并返回
        return (allCity - beginCity).pop()


Solution().destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]])
