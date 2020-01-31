class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        newversion1 = version1.split('.')
        newversion2 = version2.split('.')
        len1 = len(newversion1)
        len2 = len(newversion2)
        if len1 > len2:
            for i in range(len1):
                if i<len2:
                    if int(newversion1[i]) > int(newversion2[i]):
                        return 1
                    elif int(newversion1[i]) < int(newversion2[i]):
                        return -1
                elif int(newversion1[i]) > 0:
                    print('333')
                    return 1
            return 0

        elif len1 < len2:
            for i in range(len2):
                if i<len1:
                    if int(newversion1[i]) > int(newversion2[i]):
                        return 1
                    elif int(newversion1[i]) < int(newversion2[i]):
                        return -1
                if int(newversion2[i]) > 0:
                    print('3333')
                    return -1
            return 0
        elif len1 == len2:
            for i in range(len1):
                if int(newversion1[i]) > int(newversion2[i]):
                    return 1
                elif int(newversion1[i]) < int(newversion2[i]):
                    return -1
            return 0


if __name__ == '__main__':
    xxx = Solution()
    xxx.compareVersion('1', '1.1')


