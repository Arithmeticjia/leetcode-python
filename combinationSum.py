class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 特例判定
        if not candidates:
            return []
        n = len(candidates)
        res = []
        # 排序
        candidates.sort()

        # i: 索引；tmp: 某个解列表
        def helper(i, tmp, target):
            if target == 0:
                res.append(tmp)
                return
            if i == n or target < candidates[i]:
                return
            helper(i, tmp+[candidates[i]], target-candidates[i])
            helper(i+1, tmp, target)
        helper(0, [], target)
        return res


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
