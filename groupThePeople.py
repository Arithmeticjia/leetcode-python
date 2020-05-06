from collections import defaultdict
import collections
from typing import List
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # 初始化字典
        # value是list
        # groups = collections.defaultdict(list)
        # for i, _id in enumerate(groupSizes):
        #     groups[_id].append(i)
        groups = {}
        for i, _id in enumerate(groupSizes):
            # 键存在返回值
            # 键不存在返回默认的值
            groups.setdefault(_id, []).append(i)
        # {3: [0, 1, 2, 3, 4, 6], 1: [5]})
        # 粗分组一下
        print(groups)
        ans = list()
        for gsize, users in groups.items():
            for it in range(0, len(users), gsize):
                ans.append(users[it: it + gsize])
        return ans


print(Solution().groupThePeople(
    [3, 3, 3, 3, 3, 1, 3]))
