from collections import defaultdict
import collections
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # 初始化字典
        # value是list
        groups = collections.defaultdict(list)
        for i, _id in enumerate(groupSizes):
            groups[_id].append(i)
        # {3: [0, 1, 2, 3, 4, 6], 1: [5]})
        # 粗分组一下
        ans = list()
        for gsize, users in groups.items():
            for it in range(0, len(users), gsize):
                ans.append(users[it: it + gsize])
        return ans


print(Solution().groupThePeople(
    [3, 3, 3, 3, 3, 1, 3]))
