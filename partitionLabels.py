class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result = []
        index = {}                          # 这是一个字典
        for i in range(len(S)):
            s = S[i]
            index[s] = i
        print(index)

        '''n = index['{0}'.format(S[0])]+1
        for j in range(n):
            if index[S[j]] > n:
                n += 1
            else:
                result.append(S[j])
        print(n,result)'''
        '''for i in range(len(S)):
            length += 1
            if i == tag:
                result.append(length)
                length = 0
                if i!=len(S) - 1:
                    tag = index[S[i+1]]
            else:
                if index[S[i]] > tag:
                    tag = index[S[i]]'''
        length = -1
        tag = index[S[0]]
        for i in range(len(S)):
                #length += 1
            if index[S[i]] > tag:
                tag = index[S[i]]
            elif i == tag :
                result.append(i-length)
                length = i
                if i!=len(S) - 1:
                    tag = index[S[i+1]]
        print(result)
        return result



Solution().partitionLabels('ababcbacadefegdehijhklij')