class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        for i in range(len(A) - 1, -1, -1):
            # result_new = K + A[i]
            # A[i] = result_new % 10
            # K = result_new // 10
            K, A[i] = divmod(A[i]+K, 10)
            if K == 0:
                return A
        else:
            for j in range(1, len(str(K)) + 1):
                A.insert(0, K % 10)
                K = K // 10
        return A


if __name__ == '__main__':
    print(Solution().addToArrayForm([1, 2, 0, 0], 34))